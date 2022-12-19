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
 - name: Max-Planck-Institüt für Astrophysik, Karl-Schwarzschild-Str. 1, 85741 Garching, Germany
   index: 1
date: 19 December 2022
bibliography: paper.bib

---

# Summary

The number of available constraints on the Universe during and before cosmic reionization is grapidly growing. 
These are often scattered across inhomogeneous formats, unit systems and sampling strategies. In this paper I introduce 
`CoReCon`, a python package designed to provide a growing set of constraints on key physical quantities related to the EoR 
and a platform for the high-redshift research community to collect and store, in an open way, current and forthcoming 
observational constraints. 

# Statement of Need

The Epoch of Reionization (EoR) is the last global phase transition in the history of the Universe, 
and it represents the current frontier in the study of galaxy formation, as it radically altered the
environment in which cosmic structures formed and evolved thereafter. 
It transformed the intergalactic medium (IGM) that fills the space between 
galaxies from a cold and neutral gas to a hot and ionized one (for a review see @eorreview).
Despite its importance, little is known about this period of time, mostly as a consequence of the 
intrinsic difficulties in observing such a distant epoch. This is now rapidly changing thanks to the
*James Webb Space Telescope*, which is providing exquisite observations of the high-redshift Universe 
(see e.g. @Furtak2022, @Donnan2022, @Finkelstein2022, @Naidu2022, @Harikane22a, @Endsley2022, @Chen2022, 
@Curti2022, @Laporte2022, @Lee2022, @RB2022). 

To gain some insight on the EoR, a plethora of different
methods have been devised to extract information from the limited observations available.
However, these data are typically scattered in many different publications, using 
inhomogeneous unit systems, and sampling strategies (e.g. volume- or mass-averaged quantities in
the intergalactic medium). Hence, employing these data in a scientifically-sound way
often requires (i) retrieving the aforementioned information from different publications, and
(ii) homogenise them. The situation is made worse by the fact that derived constraints are often 
not explicitly reported (although this is slowly changing), forcing their retrieval from published 
*plots* when the authors are unavailable (e.g. because they haved moved on to a different career) 
or unwilling to share the data, a tedious and error-prone task and a sub-standard scientific practice. 

I tackle these
issues through a systematic collection of published constraints on physical properties of the Universe during 
the EoR. This collection is wrapped in a python module named `CoReCon (acronym for Collection of Reionization Constraint) that 
I present in this paper. I start by introducing the goals and design choices of `CoReCon`, then move 
on to a description of its features, followed by a review of the available constraints at the time of 
publication. I close this paper discussing desirable future developments and with a pledge to the community.


# Overview

The goal of `CoReCon` is twofold. First, it comprises a growing
set of constraints on key physical quantities related to the EoR, homogenised in their format
and units, lifting the busy researchers from the burden of searching, retrieving and formatting
data. Second, and foremost, `CoReCon` provides a platform for the high-redshift 
research community to collect and store, in an open way, such observational constraints. I do 
so by providing a Python
infrastructure, which is able to load formatted data files and provides simple utility functions
to deal with such data. The data files loaded by `CoReCon` are purposedly simple in their form and 
as complete as possible in their content, in order to collect all the relevant information in one place. 
Notably, they are required to contain a URL to the original publication and a short description of 
the methods used to retrieve the constraints from observed data. They are also allowed to contain any 
additional, unplanned-for data field, in order to reach the highest degree of flexibility and to allow
the storage of all relevant information.
Ideally, once a new constraint is published, the author of the publication will update `CoReCon`
with the relevant data. If this procedure becomes customary, `CoReCon` will serve as an up-to-date 
repository of easy-to-retrieve constraints.

To our knowledge, this is the first module of its kind - at least in the EoR community. With a similar 
spirit, there exist a collection of all the known quasars above a redshift of 5.7 (@qsolist) and a 
compilation of galaxy data for the specific purpose of validating the VELOCIraptor halo finder (@velociraptor_validation_data). Additionally, 
an effort toward openness of research in the EoR field recently materialized into an open analysis
pipeline for the reduction of spectra taken in most of the major telescopes in the world (@pypelt).

In its development version, `CoReCon`  has been used for the scientific analysis of the THESAN simulations 
(@Garaldi2022, @Kannan2022, @Smith2022) and is being used in upcoming scietific projects. 


# Features

`CoReCon` is written as a Python module in order to provide portability, ease of installation and use, 
and to reach the large community of researchers using Python. Additionally, I put effort into
building a template for entering new data to the module, which strives to be simultaneously 
easy to fill and complete in its content.

The `CoReCon` module is able to read two different data layouts, and internally transforms them into the
frontend data format exposed to the user. The module also includes simple utility functions that can transform 
the available data in commonly-used ways. For instance, selecting only the constraint on a specific 
physical quantity, in a user-defined redshift range, or transforming their layout to be ready-to-plot using
the `matplotlib` Python module.

`CoReCon` has been developed with openness in mind. For this reason, new constraints can be easily added by
simply filling a form provided, and copying it into the directory tree of the module. Data entries
are required to contain the reference and a link to the original publication, in order to ensure the original
publication is acknowledged, a *quality* flag which specifies if the data were explicitly available in the
publication or has been retrieved in some indirect way (e.g. from a published plot, hence potentially introducing 
errors[^1]), and a short description of the constraints themselves and of the method employed to measure/compute them.

The `CoReCon` module can be easily installed via `pip` and is fully documented online at [https://corecon.readthedocs.io/en/latest/](https://corecon.readthedocs.io/en/latest/). 
`CoReCon` autonomously fetches updates to the constraints at startup (but limited to once every 24 hours or when manually 
triggered to so by the user), in order to remove the requirement to maually update the entire package to obtain new constraints. 

Finally, the `CoReCon` repository features continuous integration through GitHub Actions, ensuring each new commit is 
tested and satisfies a minimal functionality level.



## Technical implementation

The main structures in `CoReCon` are the Field and DataEntry classes, respectively representing a collection of constraints on a single 
physical quantity and the constraints from an individual source (as a scientific publication). These are supplemented by a 
custom data format for the storage of the data.

The Field class is inherited from python's native dictionary class, and enrich the latter with additional variables describing 
the physical quantity represented as well as its units, commonly-adopted scientific symbol and important remarks. This 
approach was chosen in such a way to keep well separated the class members corresponding to individual constraint entries, which
are represented by the dictionary keys, and members describing the physical quantity as a whole, which are non-keys class members.
Additionally, this allowed us to include utility functions (as e.g. filter functions to select constraints based on custom criteria) 
in the class itself, allowing for an easy concatenation of them. 

Individual constraints are implemented trough the custom DataEntry class and the corresponding data format for their storage. The latter 
is thoroughly described online at [https://corecon.readthedocs.io/en/latest/](https://corecon.readthedocs.io/en/latest/), while the former 
takes care of loading the data, checking their format and expanding (when possible) fields in the native format of `CoReCon`.


# Available constraints

At the time of writing, `CoReCon` contains data for the following physical quantities: 
- *ionised fraction*. The ionised fraction of hydrogen in the Universe. Notice that this contains both volume-averaged (the majority) and
mass-averaged values. The type of average is detailed in the description of each dataset.
- *IGM temperature at mean density*. This value is typically model-dependent, as its derivation involves calibration against simulations.
- *effective optical depth of the HI and HeII Lyman-$\alpha$ forest*.
- *flux power spectrum of the Lyman-$\alpha$ forest*.
- *cosmic microwave background optical depth*.
- *UV luminosity function*. I provide the logarithm of this value and the associated errors. 
- *quasar luminosity function*.
- *column density ratio of HeII to HI*.
- *mean free path of ionizing photons*.
- *star-formation-rate density evolution*.
- *average transmitted flux quasar spectra as a function of distance from nearby galaxies*. This provides information on the sources 
(@kakiichi18, @meyer19, @meyer20) and timing (@garaldi22) of reionization. 
- *mass-metallicity relation of galaxies*, both for stellar and gas-phase metallicities.
- *galaxy main sequence* (i.e. star formation rate as a function of stellar mass).
- *UV slope*, defined as the slope of the flux density in wavelength blueward of the Lyman-$\alpha$ line.

I provide a small description of each field within `CoReCon` itself, as a string attached to each set of constraints. 

The full list of available constraints is constantly updated. Therefore I refer the reader to the 
relative [documentation page](https://corecon.readthedocs.io/en/latest/#available-constraints).


# Future work

By its nature, `CoReCon` is an ever-evolving package. Not only new constraints will constantly be published, but new instruments and 
techniques will enable the observations of new physical quantities. I will update `CoReCon` consequently to allow their inclusion. An
example of possible improvement, is the implementatino of a new data structure representing an individual astronomical object, with one or
multiple sources for its (inferred) physical properties. Relations between quantities could therefore be dynamically generated from (or
complemented by) the collection of such objects. This provides a solution to the current issue that the same object may have multiple 
entries, one for each relation in which it appears (e.g. UV luminosity function and galaxy main sequence). 

Another foreseen improvement is the integration of `CoReCon` with the pandas module (@pandas), in oder to return a pandas DataFrame when 
fetching a constraint. This will open up the possibility to employ the wide array of feaure available through pandas within `CoReCon`.

Finally, I plan to include informations about the cosmology and initial mass function assumed in deriving constraints, alongside functionalities to convert 
the data to a target cosmology or initial mass function.


# Pledge to the EoR community

`CoReCon` is an open and collaborative project by its own nature. I strongly believe it can be an useful tool for the EoR community, but it 
can only thrive and be so through collaborative effort. I ask everyone that finds this module useful for their research to contribute and 
enrich the constraints collection providing new entries.


# Acknowledgements

I acknowledge in advance the community that -- I am sure -- will help making `CoReCon` a complete and valuable module.
I am grateful to Benedetta Ciardi, Martin Glatzle, Aniket Bhagwat and Adam Schaefer for useful comments, discussions and beta-testing. 
I am thankful to the community  developing and maintaining the `numpy` (@numpy) software package, upon which `CoReCon` is built, and
`matplotlib` (@matplotlib), employed for the data visualization in the `CoReCon` documentation.



[^1]: While ideally I would like to simply ignore the data that are not available through the published paper or the authors themselves,
this would limit significantly the number of constraints available. In addition, in many cases the retrieve data are quite faithful 
to the original values. I have tested this by retrieving data from plots in publications that also reported the numerical values, and 
compared the two. Finally, I notice that I provide the option of filtering the data based on thier retrieval method, in order to 
leave the users the freedom to choose which constraints to rely on.


# References


