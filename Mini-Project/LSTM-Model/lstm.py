import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class LSTMCell(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(LSTMCell, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Gates: input, forget, cell, output
        self.gates = nn.Linear(input_size + hidden_size, 4 * hidden_size)

    def forward(self, x, hidden):
        h, c = hidden

        # Combine input and hidden state
        combined = torch.cat((x, h), dim=1)

        # Calculate gates
        gates = self.gates(combined)
        input_gate, forget_gate, cell_gate, output_gate = gates.chunk(4, dim=1)

        # Apply activations
        input_gate = torch.sigmoid(input_gate)
        forget_gate = torch.sigmoid(forget_gate)
        cell_gate = torch.tanh(cell_gate)
        output_gate = torch.sigmoid(output_gate)

        # Update cell state
        c = forget_gate * c + input_gate * cell_gate

        # Update hidden state
        h = output_gate * torch.tanh(c)

        return h, c


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.cells = nn.ModuleList(
            [
                LSTMCell(input_size if i == 0 else hidden_size, hidden_size)
                for i in range(num_layers)
            ]
        )

        self._init_weights()

    def _init_weights(self):
        for param in self.parameters():
            if param.dim() > 1:
                nn.init.xavier_uniform_(param)

    def forward(self, x, hidden=None):
        batch_size, seq_len, _ = x.size()

        if hidden is None:
            h = torch.zeros(self.num_layers, batch_size, self.hidden_size).to(x.device)
            c = torch.zeros(self.num_layers, batch_size, self.hidden_size).to(x.device)
        else:
            h, c = hidden

        output = []
        for t in range(seq_len):
            x_t = x[:, t, :]
            for i, cell in enumerate(self.cells):
                h[i], c[i] = cell(x_t, (h[i], c[i]))
                x_t = h[i]
            output.append(h[-1])

        output = torch.stack(output, dim=1)
        return output, (h, c)


# Test the LSTM implementation
def test_lstm():
    # Set random seed for reproducibility
    torch.manual_seed(42)

    # Define model parameters
    input_size = 10
    hidden_size = 20
    num_layers = 2
    seq_length = 5
    batch_size = 3

    # Create LSTM model
    lstm = LSTM(input_size, hidden_size, num_layers)

    # Create random input
    x = torch.randn(batch_size, seq_length, input_size)

    # Forward pass
    output, (h, c) = lstm(x)

    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Hidden state shape: {h.shape}")
    print(f"Cell state shape: {c.shape}")

    # Check if output shapes are correct
    assert output.shape == (
        batch_size,
        seq_length,
        hidden_size,
    ), "Output shape is incorrect"
    assert h.shape == (
        num_layers,
        batch_size,
        hidden_size,
    ), "Hidden state shape is incorrect"
    assert c.shape == (
        num_layers,
        batch_size,
        hidden_size,
    ), "Cell state shape is incorrect"

    print("All shape checks passed!")

    # Test with a simple sequence prediction task
    def generate_sequence(length):
        return torch.tensor(
            [[(i + 1) / length] for i in range(length)], dtype=torch.float32
        )

    seq_length = 10
    x_train = generate_sequence(seq_length).unsqueeze(0)  # Add batch dimension
    y_train = x_train[:, 1:, :]  # Target is the next value in the sequence

    model = LSTM(input_size=1, hidden_size=10, num_layers=1)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # Training loop
    for epoch in range(100):
        optimizer.zero_grad()
        output, _ = model(x_train)
        loss = criterion(output[:, :-1, :], y_train)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/100], Loss: {loss.item():.4f}")

    # Test the trained model
    model.eval()
    with torch.no_grad():
        test_seq = generate_sequence(seq_length).unsqueeze(0)
        predictions, _ = model(test_seq)

    print("\nTest Sequence:")
    print(test_seq.squeeze().numpy())
    print("\nPredictions:")
    print(predictions.squeeze().numpy())


if __name__ == "__main__":
    test_lstm()
