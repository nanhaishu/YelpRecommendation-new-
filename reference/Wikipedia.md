In **linear algebra**, the **singular value decomposition** (**SVD**) is a factorization of a real or complex matrix into a rotation, followed by a rescaling followed by another rotation. It generalizes the eigendecomposition of a square normal matrix with an orthonormal eigenbasis to any $ m \times n $ matrix. It is related to the polar decomposition.

Specifically, the singular value decomposition of an $ m \times n $ complex matrix $ \mathbf{M} $ is a factorization of the form 

$$
\mathbf{M} = \mathbf{U\Sigma V^*},
$$

where $ \mathbf{U} $ is an $ m \times m $ complex unitary matrix, $ \mathbf{\Sigma} $ is an $ m \times n $ rectangular diagonal matrix with non-negative real numbers on the diagonal, $ \mathbf{V} $ is an $ n \times n $ complex unitary stream, and $ \mathbf{V^*} $ is the conjugate transpose of $ \mathbf{V} $. Such decomposition always exists for any complex matrix. If $ \mathbf{M} $ is real, then $ \mathbf{U} $ and $ \mathbf{V} $ can be guaranteed to be real orthogonal matrices; in such contexts, the SVD is often denoted $ \mathbf{U \Sigma V^T} $.

The diagonal entries $ \sigma_i = \Sigma_{ii} $ of $ \mathbf{\Sigma} $ are uniquely determined by $ \mathbf{M} $ and are known as the singular values of $ \mathbf{M} $. The number of non-zero singular values is equal to the rank of $ \mathbf{M} $. The columns of $ \mathbf{U} $ and the columns of $ \mathbf{V} $ are called left-singular vectors and right-singular vectors of $ \mathbf{M} $, respectively. They form two sets of orthonormal bases $ \mathbf{u_1, \ldots, u_m} $ and $ \mathbf{v_1, \ldots, v_n,} $ and if they are sorted so that the singular values $ \sigma_i $ with value zero are all in the highest-numbered columns (or rows), the singular value decomposition can be written as

$$
\mathbf{M} = \sum_{i=1}^{r}\sigma_i\mathbf{u}_i\mathbf{v}_i^{*},
$$

where $ r \leq \min\{m,n\} $ is the rank of $ \mathbf{M} $.

The SVD is not unique, however, it is always possible to choose the decomposition such that the singular values $ \Sigma_{ii} $ are in descending order. In this case, $ \mathbf{\Sigma} $ (but not $ \mathbf{U} $ and $ \mathbf{V} $) is uniquely determined by $ \mathbf{M} $.

The term sometimes refers to the **compact SVD**, a similar decomposition $ \mathbf{M} = \mathbf{U\Sigma V}^* $ in which $ \mathbf{\Sigma} $ is square diagonal of size $ r \times r, $ where $ r \leq \min\{m,n\} $ is the rank of $ \mathbf{M} $, and has only the non-zero singular values. In this variant, $ \mathbf{U} $ is an $ m \times r $ semi-unitary matrix and $ \mathbf{V} $ is an $ n \times r $ semi-unitary matrix, such that 

$$
\mathbf{U^* U} = \mathbf{V^* V} = \mathbf{I_r}.
$$

Mathematical applications of the SVD include computing the pseudoinverse, matrix approximation, and determining the rank, range, and null space of a matrix. The SVD is also extremely useful in all areas of science, engineering, and statistics, such as signal processing, least squares fitting of data, and process control.

## Intuitive interpretations

### Rotation, coordinate scaling, and reflection

In the special case when $ \mathbf{M} $ is an $ m \times m $ real square matrix, the matrices $ \mathbf{U} $ and $ \mathbf{V^*} $ can be chosen to be real $ m \times m $ matrices too. In that case, "unitary" is the same as "orthogonal". Then, interpreting both unitary matrices as well as the diagonal matrix, summarized here as $ \mathbf{A,} $ as a linear transformation $ \mathbf{x} \mapsto \mathbf{Ax} $ of the space $ \mathbf{R_m,} $ the matrices $ \mathbf{U} $ and $ \mathbf{V^*} $ represent rotations or reflection of the space, while $ \mathbf{\Sigma} $ represents the scaling of each coordinate $ \mathbf{x_i} $ by the factor $ \sigma_i. $ Thus the SVD decomposition breaks down any linear transformation of $ \mathbf{R^m} $ into a composition of three geometrical transformations: a rotation or reflection $ \mathbf{V^*}, $ followed by a coordinate-by-coordinate scaling $ \mathbf{\Sigma}, $ followed by another rotation or reflection $ \mathbf{U}. $

Here's the converted example and sections on the SVD and spectral decomposition, adapted to Markdown and including the formatting for the equations:

---

## Example

Consider the $4 \times 5$ matrix:

$$
\mathbf{M} = \begin{bmatrix}
  1 & 0 & 0 & 0 & 2 \\
  0 & 0 & 3 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 \\
  0 & 2 & 0 & 0 & 0
\end{bmatrix}
$$

A singular value decomposition of this matrix is given by $ \mathbf{U} \mathbf{\Sigma} \mathbf{V}^* $:

$$
\begin{align}
\mathbf{U} &= \begin{bmatrix}
  0 & -1 & 0 & 0 \\
  -1 & 0 & 0 & 0 \\
  0 & 0 & 0 & -1 \\
  0 & 0 & -1 & 0
\end{bmatrix} \\[6pt]

\mathbf{\Sigma} &= \begin{bmatrix}
  3 & 0 & 0 & 0 & 0 \\
  0 & \sqrt{5} & 0 & 0 & 0 \\
  0 & 0 & 2 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0
\end{bmatrix} \\[6pt]

\mathbf{V}^* &= \begin{bmatrix}
   0 & 0 & -1 & 0 & 0 \\
  -\sqrt{0.2} & 0 & 0 & 0 & -\sqrt{0.8} \\
   0 & -1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 \\
  -\sqrt{0.8} & 0 & 0 & 0 & \sqrt{0.2}
\end{bmatrix}
\end{align}
$$

The scaling matrix $ \mathbf{\Sigma} $ is zero outside of the diagonal. Furthermore, because the matrices $ \mathbf{U} $ and $ \mathbf{V}^* $ are unitary, multiplying by their respective conjugate transposes yields identity matrices. In this case, because $ \mathbf{U} $ and $ \mathbf{V}^* $ are real valued, each is an orthogonal matrix.

$$
\begin{align}
  \mathbf{U} \mathbf{U}^* &=
  \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
  \end{bmatrix} = \mathbf{I}_4 \\[6pt]
  \mathbf{V} \mathbf{V}^* &=
  \begin{bmatrix}
    1 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 1
  \end{bmatrix} = \mathbf{I}_5
\end{align}
$$

This particular singular value decomposition is not unique. Choosing $ \mathbf{V} $ such that

$$
\mathbf{V}^* = \begin{bmatrix}
         0 & 1 & 0 & 0 & 0 \\
         0 & 0 & 1 & 0 & 0 \\
  \sqrt{0.2} & 0 & 0 & 0 & \sqrt{0.8} \\
  \sqrt{0.4} & 0 & 0 & \sqrt{0.5} & -\sqrt{0.1} \\
  -\sqrt{0.4} & 0 & 0 & \sqrt{0.5} & \sqrt{0.1}
\end{bmatrix}
$$

is also a valid singular value decomposition.

## SVD and Spectral Decomposition

### Singular values, singular vectors, and their relation to the SVD

A non-negative real number $ \sigma $ is a **singular value** for $ \mathbf{M} $ if and only if there exist unit-length vectors $ \mathbf{u} $ in $ K^m $ and $ \mathbf{v} $ in $ K^n $ such that:

$$
\begin{align}
\mathbf{Mv} &= \sigma \mathbf{u}, \\
\mathbf{M}^*\mathbf{u} &= \sigma \mathbf{v}.
\end{align}
$$

The vectors $ \mathbf{u} $ and $ \mathbf{v} $ are called **left-singular** and **right-singular vectors** for $ \sigma $, respectively.

In any singular value decomposition

$$
\mathbf{M} = \mathpt{\mathbf{U} \mathbf{\Sigma} \mathbf{V}^*}
$$

the diagonal entries of $ \mathbf{\Sigma} $ are equal to the singular values of $ \mathbf{M} $. The first $ p = \min(m,n) $ columns of $ \mathbf{U} $ and $ \mathbf{V} $ are, respectively, left- and right-singular vectors for the corresponding singular values. Consequently, the above theorem implies that:

- An $ m \times n $ matrix $ \mathbf{M} $ has at most $ p $ distinct singular values.
- It is always possible to find a unitary basis $ \mathbf{U} $ for $ K^m $ with a subset of basis vectors spanning the left-singular vectors of each singular value of $ \mathbf{M} $.
- It is always possible to find a unitary basis $ \mathbf{V} $ for $ K^n $ with a subset of basis vectors spanning the right-singular vectors of each singular value of $ \mathbf{M} $.

A singular value for which we can find two left (or right) singular vectors that are linearly independent is called "degenerate". If $ \mathbf{u}_1 $ and $ \mathbf{u}_2 $ are two left-singular vectors which both correspond to the singular value $ \sigma $, then any normalized linear combination of the two vectors is also a left-singular vector corresponding to the singular value $ \sigma $. The similar statement is true for right-singular vectors. The number of independent left and right-singular vectors coincides, and these singular vectors appear in the same columns of $ \mathbf{U} $ and $ \mathbf{V} $ corresponding to diagonal elements of $ \mathbf{\Sigma} $ all with the same value $ \sigma $.

### Relation to Eigenvalue Decomposition

The singular value decomposition is very general in that it can be applied to any $ m \times n $ matrix, whereas eigenvalue decomposition can only be applied to square diagonalizable matrices. Nevertheless, the two decompositions are related. If $ \mathbf{M} $ has SVD $ \mathbf{M} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^* $, the following two relations hold:

$$
\begin{align}
\mathbf{M}^* \mathbf{M} &= \mathbf{V} (\mathbf{\Sigma}^* \mathbf{\Sigma}) \mathbf{V}^*, \\
\mathbf{M} \mathbf{M}^* &= \mathbf{U} (\mathbf{\Sigma} \mathbf{\Sigma}^*) \mathbf{U}^*.
\end{align}
$$

The right-hand sides of these relations describe the eigenvalue decompositions of the left-hand sides. Consequently:

- The columns of $ \mathbf{V} $ (referred to as right-singular vectors) are eigenvectors of $ \mathbf{M}^* \mathbf{M} $.
- The columns of $ \mathbf{U} $ (referred to as left-singular vectors) are eigenvectors of $ \mathbf{M} \mathbf{M}^* $.
- The non-zero elements of $ \mathbf{\Sigma} $ (non-zero singular values) are the square roots of the non-zero eigenvalues of $ \mathbf{M}^* \mathbf{M} $ or $ \mathbf{M} \mathbf{M}^* $.

In the special case of $ \mathbf{M} $ being a normal matrix, and thus also square, the spectral theorem ensures that it can be unitarily diagonalized using a basis of eigenvectors, and thus decomposed as $ \mathbf{M} = \mathbf{U} \mathbf{D} \mathbf{U}^* $ for some unitary matrix $ \mathbf{U} $ and diagonal matrix $ \mathbf{D} $ with complex elements $ \sigma_i $ along the diagonal. When $ \mathbf{M} $ is positive semi-definite, $ \sigma_i $ will be non-negative real numbers so that the decomposition $ \mathbf{M} = \mathbf{U} \mathbf{D} \mathbf{U}^* $ is also a singular value decomposition. Otherwise, it can be recast as an SVD by moving the phase $ e^{i\varphi} $ of each $ \sigma_i $ to either its corresponding $ \mathbf{V}_i $ or $ \mathbf{U}_i $. The natural connection of the SVD to non-normal matrices is through the polar decomposition theorem: $ \mathbf{M} = \mathbf{S} \mathbf{R}, $ where $ \mathbf{S} = \mathbf{U} \mathbf{\Sigma} \mathbf{U}^* $ is positive semi-definite and normal, and $ \mathbf{R} = \mathbf{U} \mathbf{V}^* $ is unitary. Thus, except for positive semi-definite matrices, the eigenvalue decomposition and SVD of $ \mathbf{M} $, while related, differ: the eigenvalue decomposition is $ \mathbf{M} = \mathbf{U} \mathbf{D} \mathbf{U}^{-1}, $ where $ \mathbf{U} $ is not necessarily unitary and $ \mathbf{D} $ is not necessarily positive semi-definite, while the SVD is $ \mathbf{M} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^*, $ where $ \mathbf{\Sigma} $ is diagonal and positive semi-definite, and $ \mathbf{U} $ and $ \mathbf{V} $ are unitary matrices that are not necessarily related except through the matrix $ \mathbf{M}. $ While only non-defective square matrices have an eigenvalue decomposition, any $ m \times n $ matrix has a SVD.

### Total least squares minimization
A total least squares problem seeks the vector $ \mathbf{x} $ that minimizes the 2-norm of a vector $ \mathbf{A} \mathbf{x} $ under the constraint $ \| \mathbf{x} \| = 1 $. The solution turns out to be the right-singular vector of $ \mathbf{A} $ corresponding to the smallest singular value.

### Range, null space and rank
Another application of the SVD is that it provides an explicit representation of the range and null space of a matrix $ \mathbf{M} $. The right-singular vectors corresponding to vanishing singular values of $ \mathbf{M} $ span the null space of $ \mathbf{M} $ and the left-singular vectors corresponding to the non-zero singular values of $ \mathbf{M} $ span the range of $ \mathbf{M} $. For example, in the above example, the null space is spanned by the last row of $ \mathbf{V}^* $ and the range is spanned by the first three columns of $ \mathbf{U} $.

As a consequence, the rank of $ \mathbf{M} $ equals the number of non-zero singular values, which is the same as the number of non-zero diagonal elements in $ \mathbf{\Sigma} $. In numerical linear algebra, the singular values can be used to determine the 'effective rank' of a matrix, as rounding error may lead to small but non-zero singular values in a rank deficient matrix. Singular values beyond a significant gap are assumed to be numerically equivalent to zero.

### Low-rank matrix approximation
Some practical applications need to solve the problem of approximating a matrix $ \mathbf{M} $ with another matrix $ \tilde{\mathbf{M}} $, said to be truncated, which has a specific rank $ r $. In the case that the approximation is based on minimizing the Frobenius norm of the difference between $ \mathbf{M} $ and $ \tilde{\mathbf{M}} $ under the constraint that $ \operatorname{rank}(\tilde{\mathbf{M}}) = r $, it turns out that the solution is given by the SVD of $ \mathbf{M} $, namely:

$$
\tilde{\mathbf{M}} = \mathbf{U} \tilde{\mathbf{\Sigma}} \mathbf{V}^*,
$$

where $ \tilde{\mathbf{\Sigma}} $ is the same matrix as $ \mathbf{\Sigma} $ except that it contains only the $ r $ largest singular values (the other singular values are replaced by zero). This is known as the **Eckart–Young theorem**, as it was proved by those two authors in 1936.

### Separable models
The SVD can be thought of as decomposing a matrix into a weighted, ordered sum of separable matrices. By separable, we mean that a matrix $ \mathbf{A} $ can be written as an outer product of two vectors $ \mathbf{A} = \mathbf{u} \otimes \mathbf{v}, $ or, in coordinates, $ A_{ij} = u_i v_j $. Specifically, the matrix $ \mathbf{M} $ can be decomposed as:

$$
\mathbf{M} = \sum_i \sigma_i \mathbf{U}_i \otimes \mathbf{V}_i.
$$

Here $ \mathbf{U}_i $ and $ \mathbf{V}_i $ are the $ i $-th columns of the corresponding SVD matrices, $ \sigma_i $ are the ordered singular values, and each $ \mathbf{A}_i $ is separable. The SVD can be used to find the decomposition of an image processing filter into separable horizontal and vertical filters. Note that the number of non-zero $ \sigma_i $ is exactly the rank of the matrix.

### Nearest orthogonal matrix
It is possible to use the SVD of a square matrix $ \mathbf{A} $ to determine the orthogonal matrix $ \mathbf{O} $ closest to $ \mathbf{A} $. The closeness of fit is measured by the Frobenius norm of $ \mathbf{O} - \mathbf{A} $. The solution is the product $ \mathbf{U} \mathbf{V}^* $. This intuitively makes sense because an orthogonal matrix would have the decomposition $ \mathbf{U} \mathbf{I} \mathbf{V}^* $ where $ \mathbf{I} $ is the identity matrix, so that if $ \mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^* $ then the product $ \mathbf{A} = \mathbf{U} \mathbf{V}^* $ amounts to replacing the singular values with ones.

### The Kabsch algorithm
The Kabsch algorithm (called Wahba's problem in other fields) uses SVD to compute the optimal rotation (with respect to least-squares minimization) that will align a set of points with a corresponding set of points. It is used, among other applications, to compare the structures of molecules.

### Signal processing
The SVD and pseudoinverse have been successfully applied to signal processing, image processing, and big data (e.g., in genomic signal processing).
