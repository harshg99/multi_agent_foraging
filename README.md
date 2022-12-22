# Collaborative resource sharing with multiple foraging agents

## Abstract

we focus on the multi agent foraging task, where a group of agents collect
resources and deposit them at a central depo in a collaborative manner. Existing decentralised solutions to foraging problem
are often rule based and don’t take into account multiple objectives of exploration and exploitation for foraging, or resource
constraints in agents. Our paper’s contributions are to apply a reinforcement learning solution to the multi agent foraging
problem, which gives us the advantage of making a NP-hard foraging problem computationally feasible,decentralised and
scalable to any number of agents under resource constraints.

## Introduction

Agents would be deployed in an environment with food and water as shown in Figure 1 and each
agent will collect and deposit resources while consuming a few resources to survive. This paper aims to investigate the
emergence of behaviour that balances between exploitation of resources for individual survival and the team objective
of depositing resources at a Depo through Reinforcement Learning. Learning for Multi agent systems can be difficult
to stabilise due to non-stationarity[4] in the environment and as such we apply newer techniques in Reinforcement
Learning, specifically Proximal Policy Optimisation (PPO) to train a policy. We design and compare learned policies
over two reward structures for the problem.


## Environment

![image](https://user-images.githubusercontent.com/28558013/209136104-8468b344-3b23-4389-ace6-5423a119124b.png)

## Network Architecture

![image](https://user-images.githubusercontent.com/28558013/209136169-8fa93be7-27a9-455f-b9df-04ce8c150b50.png)

## Results

![image](https://user-images.githubusercontent.com/28558013/209136256-0a54aea4-2c55-417f-a969-68ce00cdeb11.png)

## Contributions

Harsh Goel: Environment modifications(setup,generation, resource sharing and agent observations) 
,coding up and training the models, result compilations, full-report writing 

Gaurav Kuppa: Environment setup, proofreading

Aditya Pratap Singh: Environment resource sharing Debugging, proofreading and model illustration
