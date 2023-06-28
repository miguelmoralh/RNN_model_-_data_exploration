import torch
import torch.nn as nn
import torch.optim as optim



def train_val(epochs, train_loader, val_loader, model, criterion, optimizer, device):
    losses = {"train": [], "val": []}
    best_val_loss = float('inf')  # Variable to track the best validation loss
    best_val_loss_before_patience = float('inf')  # Variable to store the best validation loss before patience
    patience = 7  # Number of epochs to wait for improvement
    counter = 0  
    for epoch in range(epochs):
        
        # Training
        model.train()  
        train_loss = 0.0
        for i, (inputs, targets) in enumerate(train_loader):
            inputs = inputs.to(device)
            targets = targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
        train_loss /= len(train_loader)
        losses['train'].append(train_loss)
        print(f'Epoch [{epoch+1}/{epochs}], Training Loss: {train_loss:.4f}')


        # Validation
        model.eval()
        with torch.no_grad():
            val_loss = 0.0
            for inputs, targets in val_loader:
                inputs = inputs.to(device)
                targets = targets.to(device)
                outputs = model(inputs)
                val_loss += criterion(outputs, targets).item()
            val_loss /= len(val_loader)
            losses['val'].append(val_loss)
            print(f'Epoch [{epoch+1}/{epochs}], Validation Loss: {val_loss:.4f}')

            # Check for early stopping
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                best_val_loss_before_patience = val_loss
                counter = 0
            else:
                counter += 1
                if counter >= patience:
                    print("Early stopping. No improvement in validation loss.")
                    break
    return train_loss, best_val_loss_before_patience, losses