import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.') 
  else:
    matrix = np.array(list)
    matrix_reshaped = matrix.reshape((3, 3))
    dictionary= {}
    dictionary['mean'] = [np.mean(matrix_reshaped, axis = 0).tolist(), np.mean(matrix_reshaped, axis = 1).tolist(), np.mean(matrix_reshaped)]
    dictionary['variance'] = [np.var(matrix_reshaped, axis = 0).tolist(), np.var(matrix_reshaped, axis = 1).tolist(), np.var(matrix_reshaped)]
    dictionary['standard deviation'] = [np.std(matrix_reshaped, axis = 0).tolist(), np.std(matrix_reshaped, axis = 1).tolist(), np.std(matrix_reshaped)]
    dictionary['max'] = [np.max(matrix_reshaped, axis = 0).tolist(), np.max(matrix_reshaped, axis = 1).tolist(), np.max(matrix_reshaped)]
    dictionary['min'] = [np.min(matrix_reshaped, axis = 0).tolist(), np.min(matrix_reshaped, axis = 1).tolist(), np.min(matrix_reshaped)]
    dictionary['sum'] = [np.sum(matrix_reshaped, axis = 0).tolist(), np.sum(matrix_reshaped, axis = 1).tolist(), np.sum(matrix_reshaped)]
    print(dictionary)
  return dictionary
