---
layout: post
comments: true
title: Stochastic programming 메모
key: 201803091
modify_date: 2018-03-09
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

$$\min_{x\in X}{g(x)=f(x)+E_\xi[Q(x, \xi)]}$$

where $$Q(x, \xi)$$ is the optimal value of the second-stage problem





 





