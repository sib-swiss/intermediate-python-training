import numpy as np

np.seterr(divide="ignore", invalid="ignore")


def computeDistanceToCentroid(points, centroid):
    """Computes the squared euclidean distance between a set
    of <points> and a <centroid>.

        * points: a 'number of dimensions'*n array.
    * centroid: a 1*'number of dimensions' array.

    The distances are returned as a 1*n array doctest strings:
    >>> p = np.array([[ 0,  0, 1, 1],[ 0,  1, 0, 1]])
    >>> c = np.array([ 0.5, 0.5])
    >>> computeDistanceToCentroid(p,c)
    array([[0.5, 0.5, 0.5, 0.5]])
    """
    distances = np.zeros([1, points.shape[1]])
    for i in range(points.shape[0]):
        distances += np.power(points[i,] - centroid[i], 2)
    return distances


def computeNearestCentroid(points, centroids):
    """computes the closest <centroid> for each point in <points>
    * points: a 'number of dimensions'*n array.
    * centroid: a 1*'number of dimensions' array.

    The closest are returned as a 1*n array that contains the index of the
        closest centroid doctest strings:
    >>> p = np.array([[ 0,  0, 1, 1],[ 0,  1, 0, 1]])
    >>> c = [ np.array([ -0.5, 0.5]) , np.array([ 1.5, 0.5]) ]
    >>> computeNearestCentroid(p,c)
    array([0, 0, 1, 1])
    """

    nbPoints = points.shape[1]
    nbCentroids = len(centroids)

    # 1. computing distances
    distances = np.empty([nbCentroids, nbPoints])
    for i in range(nbCentroids):
        distances[i,] = computeDistanceToCentroid(points, centroids[i])

    # 2. finding the closest centroid for each point
    closestCentroid = np.apply_along_axis(np.argmin, 0, distances)

    return closestCentroid


def computeCentroids(points, assignments, k):
    """computes the centroids for <points> with a given <assignment>
    * points: a 'number of dimensions'*n array
    * assignments: a 1*n array containing indexes from 0 to <k>

    Centroids are returned as a list of 'number of dimensions'*1 arrays
    doctest strings:
    >>> p = np.array([[ 0,  0, 1, 1],[ 0,  1, 0, 1]])
    >>> a = np.array([0, 0, 1, 1])
    >>> computeCentroids( p , a , 2 )
    [array([0. , 0.5]), array([1. , 0.5])]
    """
    nbDim = points.shape[0]
    nbPoint = points.shape[1]

    centroids = [np.zeros(nbDim) for i in range(k)]
    clusterSize = [0] * k

    # Summing all values.
    for i in range(nbPoint):
        cluster = assignments[i]
        centroids[cluster] += points[:, i]
        clusterSize[cluster] += 1

    # Dividing by cluster size.
    for i in range(k):
        centroids[i] /= clusterSize[i]

    return centroids


def KmeanRound(points, centroids):
    """
    For each point, compute the nearest centroid.
    Then computes new centroids based on the assignment.

    * points: a 'number of dimensions'*n array.
    * centroids: a list of 1*'number of dimensions' array.

    Returns :
    * the new centroids : list of 'number of dimensions'*1 arrays.
    * new assignment : as a 1*n array containing indexes from 0 to k.
    """

    assignment = computeNearestCentroid(points, centroids)
    newCentroids = computeCentroids(points, assignment, len(centroids))
    return newCentroids, assignment


def Kmeans(pts, k, maxNbRounds=1000, assignment=None):
    """
    <pts> is a 'nb points' * 'nb of dimensions'
    <k> : number of clusters
    <maxNbRounds> : maximum number of Kmeans round to perform

    Returns a cluster assignment : as a 1*n array containing indexes
        from 0 to k
    """
    points = pts.T
    nbPoints = points.shape[1]

    # 1. initialization
    if assignment is None:
        # we use the random assignment here.
        assignment = np.random.randint(0, k, nbPoints)

    centroids = computeCentroids(points, assignment, k)
    round = 1

    while round < maxNbRounds:
        centroids, newAssignment = KmeanRound(points, centroids)

        nbChanged = np.sum(newAssignment != assignment)

        assignment = newAssignment

        if nbChanged == 0:  # Nothing has changed -> we have converged !
            break
        elif nbChanged == nbPoints:
            # Something fishy occurs -> redraw random points to allow convergence
            assignment = np.random.randint(0, k, nbPoints)
            centroids = computeCentroids(points, assignment, k)

        # print("round {}, {:.2%} points changed assignment".format(round,nbChanged/nbPoints))
        round += 1
        # plotClusters( points , assignment , assignment , dimX=0 , dimY=1 )
        # plt.show()

    return assignment
