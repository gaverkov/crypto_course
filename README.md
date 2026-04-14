# Cryptography SoSe 2026

## Organizational stuff

We have lectures and exercise classes, but no tutorial sessions. Florian will be giving the exercise classes.

Are the lecture and exercise times convenient for you? Please let me know if they are not.  
If you do not plan to attend the lectures anyway, please tell me that as well.

Is the exam time convenient for you?

## Prerequisites

Mathematics is the language of cryptography.  
It is a general language, used not only in cryptography but also in many other areas, and it serves to formulate precise statements.

From past experience, I would say that the biggest challenge for students is the ability to make clear mathematical statements. There are true statements and false statements, but there is also a third category: inconsistent, ambiguous, unclear, or incomplete sentences whose truth value cannot be determined.

Compare this to programming:

- there is code that does what it is supposed to do,
- there is code that runs but does not do what it is supposed to do,
- and there is code that does not run at all due to errors.

As a rule of thumb, I recommend the following:

- **Know the language and notation you are using.**  
  For every technical term you use, be able to explain its exact meaning.

- **Introduce everything you refer to.**  
  It happens frequently that students use symbols without defining them, making their statements impossible to interpret.

- **Mathematics is not just for geniuses.**  
  While mathematics does include very difficult problems, the basics—and this course—are not about that.
  You do not need to be a genius to understand that if your statement involves an object `A` that you have not defined, then it cannot be verified.
  This is not just mathematics; it is common sense.

- **Rely on reasoning rather than pattern guessing.**  
  If you approach problems by only trying to “guess the next step” based on previously seen examples (in an LLM-like fashion),
  the result is usually of much lower quality.
  Your personal training data is limited—you have not read the entire internet—so this strategy is unreliable.  
  Instead, complement pattern recognition with explicit reasoning.

- **Reverse your workflow when using LLMs.**  
  You may have previously used LLMs by giving them problems to solve.
  Try reversing this process: ask them to give *you* problems to solve, and let them evaluate your solutions and explain your mistakes.  
  While LLMs operate by predicting the next word, they are quite effective at identifying common errors,
  since these same mistakes have occurred millions of times in their training data.
  As a result, they can often provide useful explanations of where your reasoning went wrong.
- **LaTeX.** When writing math to an LLM, informal notation is usually fine, but can be ambiguous. Learning basic LaTeX helps ensure precision—and the LLM itself can help you learn it along the way.

# Week 1, Lecture 1

## 0. Introduction

Cryptography is about ensuring privacy when sending or storing information—a highly relevant topic in our data-driven world.

The model, at a first approximation, is this:

Alice, a sender, wants to send a **secret** message $m$ from a set of messages $M$ to Bob, the receiver. Alice and Bob want to communicate privately, so they aim to establish a communication protocol in which the message $m$ cannot be read by anyone else. We imagine that there is an eavesdropper, Eve, who tries to figure out what the message $m$ is.

Alice decides to use an injective map  
$f : M \to C$  
from the set $M$ of messages to a set $C$ of codewords, and sends  
$c = f(m)$.  

The element $c$ is known as the *ciphertext*, while $m$ is also called the *plaintext*. Even if Eve intercepts $c$, it should still be hard to determine $m$ by just looking at $c$. In other words, solving the equation  
$c = f(m)$  
for the unknown $m \in M$ should be hard. Hardness is usually defined in the language of complexity theory, but for now we rely on intuition. 
On the other hand, Bob needs access to information that allows him to recover $m$ from $c$. That is, for Bob, solving the equation $c = f(m)$ should be easy.

Normally, one has an arsenal of encryption functions parametrized by keys. Each key defines both an encryption and a decryption function. A cryptosystem is defined by specifying three finite sets $M$, $C$, and $K$ (messages, codewords, and keys), together with functions  
$e_k : M \to C$ and $d_k : C \to M$  
parametrized by keys $k \in K$, such that  
$d_k(e_k(m)) = m$  
for all $m \in M$ and all $k \in K$.  

This means that when $m \in M$ is encrypted as $c = e_k(m)$ and then $d_k$ is applied to $c$, we recover the original message $m$.

### Role of Algebra 

You have solved equations at school and, you frequently solved algebraic equations,
but now, in digital context, we need to have a setting in which we want to have a finite version of algebra, 
where our domain is a finite set. Algebra has means to introduce such domains. So, much of the cryptography is algebra driven. 


---

### Task

Check that you know the following notions:
- function  
- injective function  
- surjective function  
- bijective function  

Be able to:
- define these notions clearly,
- give examples and non-examples.

---

### Questions

- Is every function $e_k$ as above necessarily injective? Why?

- In fact, a function $f: M \to C$ is injective if and only if there exists a function $g : C \to M$ such that  
  $g(f(m)) = m$  
  holds for all $m \in M$. Can you prove this?

---

### Snapshots of some typical mathematical issues

Two typical issues in mathematical writing:

- An *inconsistent definition* of an injective function, in which objects such as $f$, $x_1$, and $x_2$ are not properly declared.
- An *incorrect definition*, where a function is evaluated on an element outside its domain (e.g., an element of the codomain).

---

### Questions from Ron on definitions and axioms

Definitions and notation are shortcuts that allow us to express mathematical statements more concisely. What matters is that all participants in a discussion agree on their meaning. 

Roughly speaking:
- **Axioms** are properties that appear in definitions.
- For example:
  - Axioms of set theory define what a set is (i.e., what operations are allowed).
  - Axioms of vector spaces define the structure of vector spaces.

---

# Week 1, Lecture 2

- Caesar's cipher: a simple historical example to introduce the topic.
- Distinction between symmetric and asymmetric cryptography (the latter is also called *public-key cryptography*).
- Why is symmetric cryptography called "symmetric"?
- Typically, one combines symmetric and asymmetric cryptography: communication starts asymmetrically and then continues symmetrically.
- Algebraic structures: groups (arbitrary, Abelian), rings (unitary, commutative), fields.

  
