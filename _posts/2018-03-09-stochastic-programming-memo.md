---
layout: post
comments: true
title: Stochastic programming 메모
key: 201803091
modify_date: 2018-03-10
picture_frame: shadow
tags:
  - Stochastic programming
---
# Stochastic programming?
In the field of mathematical optimization, **stochastic programming**
is a framework for modeling optimization problems that involves **uncertainty**.

The goal here is to find some policy that is feasible for all
(or almost all) the possible data instances and maximizes the expectation
of some function of the decisions and the random variables.

<!--more-->

## Two-stage problems
The basic idea of two-stage stochastic programming is that (optimal)
decisions should be based on data available at the time the decisions
are made and **cannot depend on future observations**.

$$\min_{x\in X}{\{g(x)=f(x)+E_\xi[Q(x, \xi)]\}}$$

where $$Q(x, \xi)$$ is the optimal value of the second-stage problem

$$\min_{y}{\{q(y, \xi) | T(\xi)x+W(\xi)y=h(\xi)\}}$$

The classical two-stage **linear** stochastic programming problems can be formulated as

$$
    \begin{array}{ll}
    \min_{x\in \Bbb R^n} & g(x)=c^T x+E_\xi[Q(x, \xi)] \\
    \text{subject to} & Ax=b \\
    \ & x\ge0 \\
    \end{array}
$$
 
where $$Q(x, \xi)$$ is the optimal value of the second-stage problem

$$
    \begin{array}{ll}
    \min_{y\in \Bbb R^m} & q(\xi)^Ty \\
    \text{subject to} & T(\xi)x+W(\xi)y=h(\xi) \\
    \ & y\ge0 \\
    \end{array}
$$
 
$$ x\in \Bbb R^n $$ is the first-stage decision variable vector. <br>
$$ y\in \Bbb R^m $$ is the second-stage decision variable vector. <br>
$$ \xi(q, T, W, h) $$ contains the data of the second-stage problem. <br>

at the first stage we have to make a "here-and-now" decision $$x$$ before the realization of the uncertain data $$\xi$$,
viewed as a random vector, is known. At the second stage, after a realization of $$\xi$$ becomes available,
we optimize our behavior by solving an appropriate optimization problem.

### Distributional assumption(분포 가정?)
The formulation of the above two-stage problem assumes that the second-stage data $$\xi$$ can be modeled as
a random vector with a known probability distribution (not just uncertain).

### Discretization
To solve the two-stage stochastic problem numerically, one often needs to assume that the random vector $$\xi$$
has a finite number of possible realizations, called scenarios, say $$\xi_1,...,\xi_K$$, with respective probability masses
$$p_1,...,p_K$$. Then the expectation in the first-stage problem's objective function can be written as the summation:
$$E[Q(x,\xi)]=\sum_{k=1}^K p_k Q(x,\xi_k)$$
and, moreover, the two-stage problem can be formulated as one large linear programming problem
(this is called the **deterministic equivalent** of the original problem).












