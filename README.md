## Algorithmic Game Theory Class Project - CSCI 7000

----
### Notes

- Primary Paper: https://arxiv.org/pdf/1910.03094.pdf
- Helpful Resources:
    - http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.17.2539&rep=rep1&type=pdf
    - http://modelai.gettysburg.edu/2013/cfr/cfr.pdf
    - https://www.quora.com/What-is-an-intuitive-explanation-of-counterfactual-regret-minimization
    - https://int8.io/counterfactual-regret-minimization-for-poker-ai/
    - https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html
    - Regret Matching: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.60.4262&rep=rep1&type=pdf
    - Second Order Value iteration: https://arxiv.org/pdf/1905.03927.pdf Preprint
    - Markov Games: https://www2.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf
----


- Notes for _Async updates with bandit feedback_ section.
    - **Difference** : For CFR or any no-regret algorithm, one needs the feedback of all the actions which are not chosen as well. Bandit ones do not. One can use it when designing an experiment acc to need.
    - **Research Direction**: Can we use SARSA type or UCB updates instead of normal bandit?
    - what is importance sampling and what effect does it bring to the experiment?
    - **Research Direction**: on-policy (given in the paper) vs off-policy RL type?
        - " _It would be natural to adapt LONR
to the on-policy RL setting by replacing the no-regret algorithm
with a multi-armed bandit one. This type of result has previously
been obtained for normal-form games [5]_ "
   
----

- Notes for Basic _Experiments_ section.
    - **Research Direction**: Normal-form games only? can it be extended? (https://vknight.org/Year_3_game_theory_course/Content/Chapter_02-Normal_Form_Games/) (https://en.wikipedia.org/wiki/Normal-form_game) 
    - can try the theoretical approach as well:
        - **Action Item**:  " _For LONR-A, while the theory requires states be chosen for update uniformly at random, we instead
run it on policy. (We add a small probability of a random action, 0.1,
to ensure adequate exploration.) Our results show that empirically
this does not prevent convergence._ "
    - Need to explore the RM settings in general. Can modify it.
    - NoSDE games: A extension of online MDPs to cater to multi agents. Problem is that there are *multiple* randomized policies which result in the state of equil. when q-values are identical for all the agents. _There is a sense of cycle when finding equil._
    
    - **Doubt** : " _In this instance, when player 1
sends, player 2 then prefers to send. This causes player 1 to prefer
to keep, which in turn causes player 2 to prefer to keep. Player 1
then prefers to send and the cycle repeats_ " ??
    - **Action Item:** " _Not shown but important is that each also is
converging to the equilibrium Q
∗
in the average Q values._ " .

    - **Research Direction**: " _This result highlights NoSDE games as a setting where it would
be interesting to theoretically study last iterate convergence in between simple normal form games [4, 41] and rich, complex settings
such as GANs [14]._ "
    - **Research Direction**: " _This simultaneously shows a
negative and positive result: increased optimism is not known to
work or be required in any other settings. Theoretically exploring
this phenomenon is an interesting direction for future work._ "
    - Dive a bit deep into the LONR-A with OMWU vs. RM++. How does it work? what is the algo? (Fig 4(b), (c))


----

- List of the Algorithms Used
    - Multiplicative Wgts. Update (also Optimistic MWU)
    - Regret Matching (also RM+)
    - Discounted CFR
    - **New Proposal in this paper**: RM++
    - **New Proposal in this paper**: LONR-V / LONR-A
    
-----

- The Grid World Experiment

---

- The Soccer Game Experiment
    - Friendly Markov game without the complexity of NoSDE games.
    - 2 player zero-sum soccer game
    - Use any regret minimizers (possibly use different policy update rules for diff algs)
    - learning is successful despite
        - for LONR-V: few algs having no-absolute-regret (what was this again?) property
        - for LONR-A: on policy state selection
----

- Future Research Directions with big ideas
    - Read the conclusion in the paper. 4-5 ideas stated.
    
---

### System Code Design

- Data Structures that the LONR system expects from an _environment_
    - actions: (agent x state) -> list of actions
    - next_states: (agent x state) -> list of states
    - transitions: (agent x init_state x action x next_state) -> probability value
    - rewards: (agent x state x action) -> real value.