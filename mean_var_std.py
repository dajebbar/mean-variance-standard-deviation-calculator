import numpy as np

def calculate(lst):
  if len(lst) < 9:
    raise ValueError ("List must contain nine numbers.")

  np_lst = np.array(lst).reshape(3, 3)

  # # First Method
  
  # calculations = {}

  # calculations['mean'] = [np_lst.mean(axis=0).tolist(), np_lst.mean(axis=1).tolist(), np_lst.mean()]
  # calculations['variance'] = [np_lst.var(axis=0).tolist(), np_lst.var(axis=1).tolist(), np_lst.var()]
  # calculations['standard deviation'] = [np_lst.std(axis=0).tolist(), np_lst.std(axis=1).tolist(), np_lst.std()]
  # calculations['max'] = [np_lst.max(axis=0).tolist(), np_lst.max(axis=1).tolist(), np_lst.max()]
  # calculations['min'] = [np_lst.min(axis=0).tolist(), np_lst.min(axis=1).tolist(), np_lst.min()]
  # calculations['sum'] = [np_lst.sum(axis=0).tolist(), np_lst.sum(axis=1).tolist(), np_lst.sum()]

  # **************************************************************************************

  # # Second Method
  
  stats_name = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
  stats_op =[np.mean, np.var, np.std, np.max, np.min, np.sum ]
  axis = [0, 1, None]
  calculations = {
      key: [stats(np_lst, axis=axis).tolist() for axis in axis]
      for (key, stats) in zip(stats_name, stats_op)
  }
  return calculations

  return calculations