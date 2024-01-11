<h2 align="center">
  SHAPE SIMILARITY
</h2>

<p align="center">
  <img alt="Workflow" src="https://github.com/nelsonwenner/shape-similarity/workflows/shapesimilarity%20ci/badge.svg">
  <img alt="Codecov" src="https://codecov.io/gh/nelsonwenner/shape-similarity/branch/master/graph/badge.svg?token=AZW2BNGG4G">
</p>

## :bulb: About
The package allows you to check the similarity between two shapes/curves, using Frechet distance together with Procrustes analysis.
Internally, `shape_similarity` works by first normalizing the curves using Procrustes analysis and then calculating Fréchet distance between the curves.

## :page_facing_up: Content
* Frechet Distance
  * In mathematics, the Fréchet distance is a measure of similarity between curves that takes into account the location and ordering of the points along the curves. Imagine a person traversing a finite curved path while walking their dog on a leash, with the dog traversing a separate finite curved path. Each can vary their speed to keep slack in the leash, but neither can move backwards. The Fréchet distance between the two curves is the length of the shortest leash sufficient for both to traverse their separate paths from start to finish. Note that the definition is symmetric with respect to the two curves—the Fréchet distance would be the same if the dog were walking its owner.
  
* Procrustes Analysis
  * In statistics, Procrustes analysis is a form of statistical shape analysis used to analyse the distribution of a set of shapes. To compare the shapes of two or more objects, the objects must be first optimally "superimposed". Procrustes superimposition (PS) is performed by optimally translating, rotating and uniformly scaling the objects. In other words, both the placement in space and the size of the objects are freely adjusted. The aim is to obtain a similar placement and size, by minimizing a measure of shape difference called the Procrustes distance between the objects.  

## :rocket: Technologies
* [Python3](https://www.python.org/)

## :package: Installation
1. Install with pip
```shell
$ python -m pip install shapesimilarity
```
2. Install from source code
```shell
$ git clone https://github.com/nelsonwenner/shape-similarity.git

$ python -m pip install .
```
3. Run the tests
```shell
$ python -m pip install pytest

$ python -m pytest
```

## :information_source: Example useage
```python
from shapesimilarity import shape_similarity
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, -1, num=200)

y1 = 2*x**2 + 1
y2 = 2*x**2 + 2

shape1 = np.column_stack((x, y1))
shape2 = np.column_stack((x, y2))

similarity = shape_similarity(shape1, shape2)

plt.plot(shape1[:,0], shape1[:,1], linewidth=2.0)
plt.plot(shape2[:,0], shape2[:,1], linewidth=2.0)

plt.title(f'Shape similarity is: {similarity}', fontsize=14, fontweight='bold')
plt.show()
```
* You can further customize the precision of the shape_similarity function by changing the rotation (default 10). Increasing it will increase accuracy. You can also disable rotation correction completely (default True).
  ```python
  # disable rotation correction entirely
  shape_similarity(shape1, shape2, checkRotation=False)

  # higher accuracy, but slower
  shape_similarity(shape1, shape2, rotation=30)
  ```

## :chart_with_downwards_trend: Results
<p align="center">
  <img alt="plot1" src="https://user-images.githubusercontent.com/40550247/126214358-6aa995aa-15b1-4c60-9f0e-34bbef91a99b.png">
  <img alt="plot2" src="https://user-images.githubusercontent.com/40550247/126214579-302d9220-98ed-4823-992b-d4439145bc5a.png">
</p>

## :pushpin: Referencies
* [Frechet distance](https://en.wikipedia.org/wiki/Fr%C3%A9chet_distance)
* [Procrustes analysis](https://en.wikipedia.org/wiki/Procrustes_analysis)
* [Curve Matcher](https://github.com/chanind/curve-matcher)

---
Made with :hearts: by Nelson Wenner :wave: [Get in touch!](https://www.linkedin.com/in/nelsonwenner/)
