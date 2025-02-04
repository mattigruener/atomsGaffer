# AtomsGaffer

The Tool Chefs have open-sourced their [Atoms Crowd](https://atoms.toolchefs.com) extension for [Gaffer](http://www.gafferhq.org).

> Note : If you are an existing Tool Chefs customer, you will be able to download pre-built AtomsGaffer binaries from the normal Atoms Crowd download page.

> Caution : This project is still a non-functional work in progress.

### Build Instructions

**Requires:**

* cmake
* Gaffer Install

**In a terminal:**

```
setenv GAFFER_ROOT <gaffer install path>
setenv ATOMS_ROOT <atoms install path>
setenv ATOMSGAFFER_INSTALL_PREFIX <your desired install path>

cd atomsGaffer
cmake -DGAFFER_ROOT=$GAFFER_ROOT -D$ATOMS_ROOT -DCMAKE_INSTALL_PREFIX=$ATOMSGAFFER_INSTALL_PREFIX .
make install -j <num cores>
```

### Runtime Instructions

Now that you've installed the extension to `$ATOMSGAFFER_INSTALL_PREFIX`, you need to tell Gaffer about it:

`setenv GAFFER_EXTENSION_PATHS $ATOMSGAFFER_INSTALL_PREFIX:$GAFFER_EXTENSION_PATHS`

Next, test your install:

`gaffer test AtomsGafferTest AtomsGafferUITest`

Now run the `gaffer` gui as normal.
