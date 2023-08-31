# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

from datetime import datetime

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "VSC documentation"
copyright = f"{datetime.now().year}, VSC (Vlaams Supercomputing Center)"
author = "VSC (Vlaams Supercomputing Center)"

# The short X.Y version
version = "2.0"
# The full version, including alpha/beta/rc tags
release = "2.0"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx_reredirects',
    'notfound.extension',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The file extensions of source files. Sphinx considers the files with this
# suffix as sources. The value can be a dictionary mapping file extensions to
# file types.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = None

# To render double dashes in text as double dashes (and not as an "en dash"):
smartquotes_action = 'qe'  # instead of default 'qDe'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Icon links on right side of the navbar
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/header-links.html#icon-links
html_navbar_icon_links = [
    {
        "name": "VSC in LinkedIn",
        "url": "https://www.linkedin.com/company/vschpc",
        "icon": "fa-brands fa-linkedin",
    },
    {
        "name": "VSC in GitHub",
        "url": "https://github.com/vscentrum",
        "icon": "fa-brands fa-square-github",
    },
    {
        "name": "VSC in Twitter",
        "url": "https://twitter.com/VSC_HPC",
        "icon": "_static/fa-square-x-twitter.svg",
        "type": "local",
    },
    {
        "name": "VSC Website",
        "url": "https://www.vscentrum.be/",
        "icon": "_static/fa-square-vsc.svg",
        "type": "local",
    },
]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "navbar_align": "left",
    "header_links_before_dropdown": 8,
    "icon_links": html_navbar_icon_links,
    "search_bar_text": "Search in VSC Docs...",
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "use_edit_page_button": True,
    "show_prev_next": False,
    "footer_start": ["copyright"],
    "footer_end": [],
    "pygment_light_style": "manni",  # toned-up comments
    "pygment_dark_style": "inkpot",  # toned-up comments
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/vsc.css']

# Logo in top bar
html_logo = "_static/vsc-docs-logo-1.png"

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "index": [],
    "**": ["search-field", "sidebar-nav-bs"],
}

# Edit this page button
html_context = {
    "github_user": "hpcleuven",
    "github_repo": "VscDocumentation",
    "github_version": "pydata",
    "doc_path": "source",
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'VSCdocumentationdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'VSCdocumentation.tex', 'VSC documentation Documentation',
     'VSC (Vlaams Supercomputing Center)', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'vscdocumentation', 'VSC documentation Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'VSCdocumentation', 'VSC documentation Documentation',
     author, 'VSCdocumentation', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- NotFound Extension ------------------------------------------------------
notfound_template = '404.html'
notfound_urls_prefix = ''

# -- Page redirects ----------------------------------------------------------
redirects = {
    "access/getting_access": "/access/vsc_account.html",
    "access/account_request": "/access/vsc_account.html",
    "access/access_and_data_transfer": "/access/access_methods.html",
    "access/upload_new_key": "/access/generating_keys.html",
    "access/data_transfer": "/data/transfer.html",
    "access/data_transfer_using_winscp": "/data/transfer/winscp.html",
    "access/data_transfer_with_filezilla": "/data/transfer/filezilla.html",
    "access/data_transfer_with_scp_sftp": "/data/transfer/scp_sftp.html",
    "access/eclipse_as_a_remote_editor": "/software/eclipse.html",
    "access/multiplatform_client_tools": "/access/access_methods.html",
    "data/tier1_data_main_index": "/data/tier1_data_service.html",
    "globus/globus_main_index": "/globus/index.html",
    "globus/globus_platform": "/globus/index.html",
    "jobs/job_submission_and_credit_reservations": "/jobs/credits.html",
    "jobs/the_job_system_what_and_why": "/jobs/index.html",
    "jobs/using_software": "/software/using_software.html",
    "leuven/data_transfer_kuleuven_network_drives": "/data/transfer/network_drives/kuleuven.html",
    "leuven/mfa_quickstart": "/access/mfa_quickstart.html",
    "leuven/tier2_hardware/mfa_login": "/access/mfa_login.html",
}

# -- MyST --------------------------------------------------------------------

myst_heading_anchors = 2
myst_enable_extensions = ["colon_fence"]

# -- RST Prolog --------------------------------------------------------------
rst_prolog = ""

# Badges
rst_prolog += """
.. |Optional| replace:: :bdg-primary:`Optional`
.. |Example| replace:: :bdg-info:`Example`
.. |Recommended| replace:: :bdg-success:`Recommended`
.. |Alert| replace:: :bdg-danger:`Alert`
.. |Warning| replace:: :bdg-warning:`Warning`
.. |Info| replace:: :bdg-info:`Info`
"""

# VSC Institute Badges
rst_prolog += """
.. |KUL| replace:: :bdg-info:`KU Leuven`
.. |UA| replace:: :bdg-danger:`UAntwerp`
.. |UG| replace:: :bdg-primary:`UGent`
.. |VUB| replace:: :bdg-warning:`VUB`
"""

# Links used multiple times across the documentation
rst_prolog += """
.. _Adaptive Computing documentation: https://support.adaptivecomputing.com/hpc-cloud-support-portal/
.. _ARM-DDT video: https://developer.arm.com/tools-and-software/server-and-hpc/debug-and-profile/arm-forge/resources/videos
.. _ARM-MAP: https://www.arm.com/products/development-tools/hpc-tools/cross-platform/forge/map
.. _atools documentation: https://atools.readthedocs.io/en/latest/
.. _Beginning Hybrid MPI/OpenMP Development: https://software.intel.com/en-us/articles/beginning-hybrid-mpiopenmp-development
.. _CP2K: https://www.cp2k.org/
.. _CPMD: http://www.cpmd.org/
.. _CUDA: https://developer.nvidia.com/cuda-zone
.. _cuDNN: https://developer.nvidia.com/cudnn
.. _Cyberduck: https://cyberduck.io
.. _Cygwin: https://www.cygwin.com/
.. _Docker: https://www.docker.com/
.. _docs.globus.org: https://docs.globus.org
.. _download FileZilla: https://filezilla-project.org/download.php?type=client
.. _Eclipse download page: http://www.eclipse.org/downloads
.. _Eclipse packages download page: https://www.eclipse.org/downloads/packages/
.. _Eclipse: https://www.eclipse.org/
.. _eligible users: https://www.vscentrum.be/getaccess
.. _FFTW documentation: http://www.fftw.org/#documentation
.. _FFTW: http://www.fftw.org/
.. _FileZilla project page: https://filezilla-project.org/
.. _GCC documentation: http://gcc.gnu.org/onlinedocs/
.. _get in touch: https://www.vscentrum.be/getintouch
.. _Globus Web Interface: https://app.globus.org/ 
.. _Globus Management Console: https://www.globus.org/app/login
.. _Globus Connect Server Installation Guide: https://docs.globus.org/globus-connect-server-installation-guide
.. _Globus How-To pages: https://docs.globus.org/how-to
.. _Globus Connect Personal: https://www.globus.org/globus-connect-personal
.. _Globus Groups How-To page: https://docs.globus.org/how-to/managing-groups
.. _Globus CLI documentation: https://docs.globus.org/cli/examples
.. _Globus-Timer-CLI on PyPi: https://pypi.org/project/globus-timer-cli
.. _Globus Python SDK documentation: https://globus-sdk-python.readthedocs.io/en/stable/index.html
.. _GNU binutils documentation: https://sourceware.org/binutils/docs/
.. _GROMACS: http://www.gromacs.org/
.. _HPE MPT documentation: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-a00037728en_us&docLocale=en_US
.. _Intel MPI Documentation: https://software.intel.com/en-us/articles/intel-mpi-library-documentation
.. _Intel MPI: https://software.intel.com/en-us/intel-mpi-library
.. _Intel Software Documentation Library: https://software.intel.com/en-us/documentation
.. _Interoperability with OpenMP API: https://software.intel.com/en-us/node/528819
.. _irods.org: https://irods.org/
.. _ITAC documentation: https://software.intel.com/en-us/articles/intel-trace-analyzer-and-collector-documentation/
.. _JellyfiSSH: http://www.m-works.co.nz/jellyfissh.php
.. _Keras: https://keras.io/
.. _LAPACK user guide: http://www.netlib.org/lapack/lug/
.. _LAPACK95 user guide: http://www.netlib.org/lapack95/lug95/
.. _Linux Basics on Lifewire : https://www.lifewire.com/learn-how-linux-basics-4102692 
.. _Linux Newbie Administrator Guide: http://lnag.sourceforge.net/
.. _Linux Tutorials YouTube Channel: https://www.youtube.com/channel/UCut99_Fv1YEcpYRXNnUM7LQ 
.. _LLNL openMP tutorial: https://computing.llnl.gov/tutorials/openMP
.. _Lmod documentation: http://lmod.readthedocs.io/en/latest/
.. _Lmod: http://lmod.readthedocs.io/en/latest/
.. _Locality-Aware Parallel Process Mapping for Multi-Core HPC Systems: http://www.joshuahursey.com/papers/2011/hursey-cluster-poster-2011.pdf
.. _MathWorks: https://nl.mathworks.com/
.. _MATLAB compiler documentation: https://nl.mathworks.com/help/compiler/index.html
.. _MKL Link Line Advisor: https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor
.. _MobaXterm: https://mobaxterm.mobatek.net
.. _MPI forum: https://www.mpi-forum.org/
.. _MPI Reference Manual: https://software.intel.com/en-us/articles/intel-mpi-library-documentation
.. _MPI Standard documents: https://www.mpi-forum.org/docs/
.. _MPICH: https://www.mpich.org/
.. _MVAPICH: http://mvapich.cse.ohio-state.edu/
.. _NAMD: http://www.ks.uiuc.edu/Research/namd/
.. _Netlib BLAS repository: http://www.netlib.org/blas/
.. _Netlib LAPACK repository: http://www.netlib.org/lapack/
.. _Netlib ScaLAPACK repository: http://www.netlib.org/scalapack/
.. _NX Client download: https://www.nomachine.com/download-enterprise#NoMachine-Enterprise-Client
.. _Open MPI Documentation: https://www.open-mpi.org/doc
.. _Open MPI Explorations in Process Affinity: https://www.slideshare.net/jsquyres/open-mpi-explorations-in-process-affinity-eurompi13-presentation
.. _Open MPI: https://www.open-mpi.org/
.. _OpenBLAS Wiki: https://github.com/xianyi/OpenBLAS/wiki
.. _OpenBLAS: https://www.openblas.net/
.. _OpenMP compilers and tools: https://www.openmp.org/resources/openmp-compilers-tools/
.. _OpenMP: https://www.openmp.org
.. _OpenSHMEM: http://www.openshmem.org/site/
.. _Paraview tutorial: https://www.vtk.org/Wiki/images/8/88/ParaViewTutorial38.pdf
.. _Paraview website: https://www.paraview.org/
.. _POSIX threads: https://en.wikipedia.org/wiki/POSIX_Threads
.. _PuTTY download site: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
.. _PuTTY: https://www.chiark.greenend.org.uk/~sgtatham/putty/
.. _qsub documentation: http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torque.htm#topics/torque/commands/qsub.htm
.. _ScaLAPACK user guide: http://netlib.org/scalapack/slug/
.. _Scalasca docs: http://www.scalasca.org/software/scalasca-2.x/documentation.html
.. _scp manual page: http://man.openbsd.org/scp
.. _Service Catalog: https://icts.kuleuven.be/sc/HPC
.. _sftp manual page: http://man.openbsd.org/sftp
.. _Singularity documentation: https://singularity.hpcng.org/user-docs/3.8/
.. _Singularity: https://singularity.hpcng.org/
.. _sbatch manual page: https://slurm.schedmd.com/sbatch.html
.. _ssh manual page: http://man.openbsd.org/ssh
.. _ssh-keygen manual page: http://man.openbsd.org/ssh-keygen
.. _ssh_config manual page: http://man.openbsd.org/ssh_config
.. _Sylabs Singularity: https://sylabs.io/singularity/
.. _TensorFlow: https://www.tensorflow.org/
.. _Threading Building Blocks: https://www.threadingbuildingblocks.org
.. _tier-1 project application: https://www.vscentrum.be/tier1
.. _TigerVNC: https://tigervnc.org/
.. _Torque 6.0.1 documentation: http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torque.htm 
.. _training waiting list: https://admin.kuleuven.be/icts/onderzoek/hpc/HPCintro-waitinglist
.. _TurboVNC download page: https://sourceforge.net/projects/turbovnc/files/
.. _TurboVNC: https://www.turbovnc.org/
.. _VirtualGL: https://en.wikipedia.org/wiki/VirtualGL
.. _VSC account page: https://account.vscentrum.be/
.. _VSC training: https://www.vscentrum.be/training
.. _WinSCP docs: https://winscp.net/eng/docs/start
.. _worker documentation: http://worker.readthedocs.io/en/latest/
.. _worker framework documentation: https://worker.readthedocs.io/en/latest/
.. _www.globus.org: https://www.globus.org
.. _Xming website: http://www.straightrunning.com/XmingNotes/
"""
