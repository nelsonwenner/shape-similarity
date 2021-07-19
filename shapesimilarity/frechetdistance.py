from .geometry import euclidean_distance

'''
Discrete Frechet distance between 2 curves
based on http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf
modified to be iterative and have better memory usage
'''

def frechet_distance(curve1, curve2):
  '''
  Args:
    polyP: polynomial representing curve 1
    polyQ: polynomial representing curve 2
  Returns:
    Frechet distance between two curves
  Descriptions:
    Calculate Frechet distance between two curves
  '''
  
  longcalcurve = curve1 if len(curve1) >= len(curve2) else curve2
  shortcalcurve = curve2 if len(curve1) >= len(curve2) else curve1

  prev_resultscalcol = []
  for i in range(0, len(longcalcurve)):
    current_resultscalcol = []
    for j in range(0, len(shortcalcurve)):
      current_resultscalcol.append(
        calc_value(
          i, j, prev_resultscalcol, 
          current_resultscalcol, 
          longcalcurve, shortcalcurve
        )
      )
    prev_resultscalcol = current_resultscalcol
  return prev_resultscalcol[len(shortcalcurve) - 1]

def calc_value(i, j, prevResultsCol, currentResultsCol, longCurve, shortCurve):
  if i == 0 and j == 0:
    return euclidean_distance(longCurve[0], shortCurve[0])
  if i > 0 and j == 0:
    return max(prevResultsCol[0], euclidean_distance(longCurve[i], shortCurve[0]))
  last_result = currentResultsCol[len(currentResultsCol) - 1]
  if i == 0 and j > 0:
    return max(last_result, euclidean_distance(longCurve[0], shortCurve[j]))
  return max(
    min(prevResultsCol[j], prevResultsCol[j - 1], last_result),
    euclidean_distance(longCurve[i], shortCurve[j])
  )