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












