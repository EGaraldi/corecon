---
title: 'CoReCon: an open, community-powered collection of Reionization constraints'
tags:
  - Python
  - astronomy
  - cosmology
  - reionization
  - constraints
authors:
  - name: Enrico Garaldi
    orcid: 0000-0002-6021-7020
    affiliation: 1
affiliations:
 - name: Post-doctoral Fellow, Max-Planck-Institüt für Astrophysik
   index: 1
date: 
bibliography: paper.bib

---

# Summary

The Epoch of Reionization (EoR) is the latest global phase change in the Universe, 
and it radically altered the environment in which galaxies formed and evolved
thereafter. Despite its importance in the history of the Universe, little is known
about such period of time, mostly as a consquence of the intrinsic difficulties in
observing such a distant epoch. The latter is the main reason why a plethora of different
methods have been devised to extract infromation from the limited observations available.
However, these data are typically scattered in many different publications, using 
inhomogeneous unit systems, and average strategies (e.g. volume- or mass-averaged quantities in
the inter-galactic medium). Hence, emplying these data in a scientifically-sound way
often requires (i) retrieving the aforementioned information from different publications, and
(ii) homogeneise them. Moreover, it is often challenging to grasp a complete picture of
available constraints for a given physical quantity. 

The goal of `CoReCon` is to provide a 
platform for the reionization and high-redshift research communities to collect observational
constraint on jey physical quantities, in an homogenous way. We do so by providing a Python
infrastructure, which is able to load formatted data files and provides simple utility functions
to deal with such data. The data files loaded by `CoReCon` are purposedly simple in their form and 
complete in their content, in order to collect all the relevant information in one place. Notably, 
they require a URL to the original publication and a short description of the methods used to 
retrieve the constraints from observed data.

To my knowledge, this is the first module of its kind. 

# Features

`CoReCon` is written as a Python module in order to provide portability, ease of installation and use, 
and to reach the large community of researcher using Python. Additionally, we put effort into 
building a template for entering new data to the module, which strives to be simultaneously 
easy to fill and complete.

The `CoReCon` module is able to read two different data layout, and internally transform them into the
frontend data format exposed to the user. It also includes simple utility functions that can transform 
the available data in commonly-used ways. For instance, selecting only the constraint on a specific 
physical quantity, in a user-defined redshift range, or transforming their layout to be ready-to-plot using
the matplotlib Python module.

`CoReCon` has been developed with openness in mind. For this reason, new constraints can be simply added by
simply filling a form provided, and adding the file into the directory tree of the module.

At the time of writing, `CoReCon` contains data for the following physical quantities: ionised fraction,
IGM temperature at mean density, effective optical depth of the HI and HeII Lyman-$\alpha$ forest,
flux power spectrum of the Lyman-$\alpha$ forest, CMB optical depth, galaxy and quasar UV luminosity 
functions, column density ratio, and mean free path of ionizing photons.

The `CoReCon` module can be easily installed via `pip`.


Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```	

# Acknowledgements

We acknowledge 

# References
