import torch
import numpy as np

def test_model(test_loader, model, criterion, device):
  
  # Testing
  model.eval()
  predictions = [] # initialize an empty list for predictions
  y_trues = [] # initialize an empty list for targets
  with torch.no_grad():
    test_loss = 0.0

    for inputs, targets in test_loader:
      inputs = inputs.to(device)
      targets = targets.to(device)
      outputs = model(inputs)
      y_pred = outputs.detach().cpu().numpy() 
      y_true = targets.detach().cpu().numpy() 
      predictions.append(y_pred) 
      y_trues.append(y_true) 
      test_loss += criterion(outputs, targets).item()
      
  predictions = np.concatenate(predictions, axis=0) 
  y_trues = np.concatenate(y_trues, axis=0) 
  test_loss /= len(test_loader)
 
  print(f'Test Loss: {test_loss:.4f}') 

  return test_loss, predictions, y_trues