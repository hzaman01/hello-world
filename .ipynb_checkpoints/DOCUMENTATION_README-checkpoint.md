# Documentation Generation Guide

This README serves as a guide for understanding and using the **documentation** commands in mew-cli.

___

## Overview
1. [Command Arguments](#command-arguments)
2. [Document Configuration Files](#document-configuration-files)
    1. [Top-Level Config](#top-level-config)
    2. [Low-Level Config](#low-level-config)
3. [Handlebars Templating Syntax](#handlebars-templating-syntax)
    1. [Inserting Thresholds and Parameters](#inserting-threshold-and-parameter-information)
    2. [Thresold and Parameter Key Words](#threshold-and-parameter-key-words)
    3. [Insert Params Placeholders](#insert-params-placeholders)
    4. [Insert JSON Tables](#insert-json-tables)
    5. [Insert Images](#insert-images)
    6. [Insert Table of Contents](#insert-table-of-contents)
    7. [Conditional Handlebars Rendering](#conditional-handlebars-rendering)
4. [Cross-references and footnotes](#cross-references-and-footnotes)
5. [Installation](#installation)
6. [Troubleshooting](#troubleshooting)

___

## Command Arguments

`-p, --path=path`
- Path to a directory containing a top-level docs.config.yaml file

`--last-updated`
- Inserts git commit information into the generated documentation
- Git commit information is inserted for each individual markdown file used to generate the documentation

---

## Document Configuration Files

The document configuration file is named `docs.config.yaml`. The `.yml` file extension is also supported.

There are two types of config files for documentation: `Top-Level` and `Low-Level`
- `Top-Level`:
    - Specifies details for building a single document for a directory (such as `/validations` or `/models`)
    - Collects information from the `Low-Level` configs into a single output document
- `Low-Level`:
    - Specifies details for an individual sub-directory
    - For example, a single Validation Test Plan, or a single Model


### Top-Level Config
```
# Example top-level docs.config.yaml file
toc_depth: 3
dir_output_path: path/to/name-of-documentations-directory
file_name: Validation_Test_Plans_doc
introduction:
  - header.md
  - introductory_paragraph.md
dir_order:
  - Test_Plan_A
  - Test_Plan_B
conclusion:
  - conclusion_file.md
  - appendix.md
template_metadata:
  title: Top-Level Title
  author: Dev
  date: 08-04-2021
  lang: en-US
  linkReferences: true
  abstract: |
    This is the abstract.

    It consists of two paragraphs.
```

The document created with this config compiles the provided contents in the following order:
1. Contents of `introduction`
2. Contents of `dir_order`
3. Contents of `conclusion`

#### Field Definition

`toc_depth`:
- Specifies the number of section levels to include in the table of contents (ToC)
- Required field to auto-generate the ToC

`dir_output_path`:
- The folder path where the output documentation is created
- Defaults to `/documentation` at root

`file_name`:
- Name of the generated output documentation file
- Defaults to `{folder_name}_documentation` using the value provided in the `-p` argument

`dir_order`:
- Order in which documentation for sub-directories will be inserted into the generated documentation
- Each line is the path from the top-level docs config file to a folder directory which contains a low-level docs config file

`introduction`:
- Ordered list of markdown files to display at the start of the generated document

`conclusion`:
- Ordered list of markdown files to display at the end of the generated document

`template_metadata`:
- Optional field used by Pandoc
- Displays additional information at the top of the generated document


### Low-Level Config
```
# Example low-level docs.config.yaml file
toc_depth: 3
dir_order:
  - Statistical_Test_1
  - Statistical_Test_2
dir_source: mysource
dir_details:
  Statistical_Test_1:
    file_order:
      - description.md
      - results.md
  Statistical_Test_2:
    ...

```

#### Field Definition

`toc_depth`:
- Specify the number of section levels to include in the table of contents (ToC)
- Required field to auto-generate the ToC

`dir_order`:
- Similar to top-level config field
- Order in which documentation for sub-directories will be displayed

`dir_source`:
- Declare the path from the folder containing the low-level config to the directory that stores all files (.md, .json) referenced in `dir_details`
- E.g if you specify `dir_source: mysource`, then files listed in `dir_details` will be read from directory `Statistical_Test_X/mysource`
- Defaults to `/docs`

`dir_details`:
- Declares details on how to collect documentation together for sub-directories
- `file_order`:
    - Order in which markdown files are displayed

---

## Handlebars Templating Syntax

### Inserting Threshold and Parameter information

Optional `gray-matter` section that can be inserted at the top of individual markdown files.
- Specify information that can dynamically be inserted into the output documents.
- Must also include the `---` delimiters

Example markdown file with gray-matter:

```
---
threshold:
  pipeline: path/to/file/dvc.yaml
  stage: prepare
  threshold_key: roc_auc
params:
  param_file: path/to/file/params.yaml
---

Example markdown file content.

```

Gray-matter Field Defintion:
- Threshold Fields:
  - `pipeline`:
    - Relative path to a dvc.yaml file which contains a stage with threshold and metric information
  - `stage`:
    - Name of the stage on the above dvc.yaml file to retrieve threshold and metric information from
  - `threshold_key`:
    - Name of the threshold key from the pipeline stage
    - Used to get the threshold value
- Parameter Fields:
  - `param_file`:
    - Path to a yaml file which contains params information


### Threshold and Parameter Key Words

Users can reference the information inserted into the above gray-matter using the following key words and syntax:

```
...
# access the path to pipeline dvc.yaml
Pipeline: {{pipeline}}

# access stage name
Stage: {{stage}}

# acceess threshold key
Threshold Key: {{thresholdKey}}

# access the corresponding threshold value
Threshold Value: {{thresholdVal}}

# access the metric value associated with the threshold key
Metric Value: {{metricVal}}

# access the path to param.yaml
Param file: {{paramFile}}
...
```

### Insert Params Placeholders

Individual parameter values from the provided `paramsFile` can also be referenced

Given params.yaml file:

```
prepare:
  split: 0.20
  seed: 20170428

featurize:
  max_features: 500
  ngrams: 1

single_ref: 123
```

Example of directly referencing parameters from the provided `paramFile`

```
---
params:
  param_file: path/to/params.yaml
---

Path to file params.yaml: {{paramFile}}
Loading params single reference: {{param "single_ref"}}
Loading params with nested object references: {{param "prepare.seed"}}
Loading params object reference: {{param "featurize"}}

```

### Insert JSON Tables

JSON files can be inserted into your markdown files as tables using the following syntax:

```
{{table "path/to/file.json"}}
```

### Insert Images

Image files can be inserted into your markdown files using the following syntax:

```
{{image "path/to/image.png"}}
```

- Supported extensions: JPEG, PNG, SVG

### Insert Table of Contents

Default behavior:
- Table of Contents (ToC) will be inserted at the top of the output documentation

Rendering ToC elsewhere in documentation:
```
{{toc number}}
```
- Leave this placeholder in any markdown file you wish to create a ToC in
- `number` specifies the table of content depth. Defaults to 3.

### Conditional Handlebars Rendering

mew-cli leverages [Handlebarsjs](https://handlebarsjs.com/guide/#what-is-handlebars) to provide flexible options for dynamically rendering markdown content

Conditional Logic Key Words:
- `gt`: greater than
- `gte`: greater than or equal
- `lt`: less than
- `lte`: less than or equal
- `eq`: equal
- `ne`: not equal

Example:
```
# Renders the block of content if the metric value is greater than or equal the threshold value
# given metricVal = 0.8
# given array thresholdVal = [0.1, 0.2, 0.3]
# Content will be displayed if 0.8 > 0.3

{{#if (gte metricVal thresholdVal.[2])}}
  <b>This is passed block content</b>
{{/if}}
```

Some other utilities key words:

`first`: get the first element of the array.

```
# display value: 0.1
{{first thresholdVal}}
```

`last`: get the last element of the array.

```
# display value: 0.3
{{last thresholdVal}}
```

## Cross-references and footnotes

Refer to [pandoc-crossref syntax documentation](http://lierdakil.github.io/pandoc-crossref/)

---

## Installation
### Install anaconda

[Anaconda](https://docs.anaconda.com/anaconda/install/linux/) should already be installed on your Platform McKinsey instance, but in the case that it needs to be installed or updated, follow these instructions.

```
# note: this is Anaconda Installation instructions for Ubuntu v18.04 distribution only
# download the anaconda installation shell script
$ curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh

# verify the Data Integrity of the Installer
$ sha256sum Anaconda3-2020.02-Linux-x86_64.sh

# run command install anaconda via the downloaded script, click YES or ENTER if any questions
$ bash Anaconda3-2020.02-Linux-x86_64.sh
```

#### Correct python and pip version
After successfully installing Anaconda, python and pip should be available for usage.
Use `python 3.7.3` and `pip 21.1.2` for support installing `DVC v2.0.6`
Ensure you correct Python and Pip version to successfully install DVC v2.0.6

```
// check python and pip version to make sure installing true version
$ python --version
$ python -m pip --version
```

Running following command if you need to upgrade pip version
```
pip install --upgrade pip
```

### Install pandoc

```
$ conda install -c conda-forge pandoc==2.12
$ pandoc --version
```

### Install pandoc-crossref

```
$ conda install -c conda-forge pandoc-crossref==0.3.10.0
$ pandoc-crossref --version
```

Check [pandoc-crossref syntaxes](http://lierdakil.github.io/pandoc-crossref/)

### Install pandoc-xnos

We use pip to install pandoc-xnos. This plugin contains many different individual filters

```
$ pip install pandoc-fignos pandoc-eqnos pandoc-tablenos pandoc-secnos
```

Check [pandoc-xnos supports](https://github.com/tomduck/pandoc-xnos/)

### Add Environment Variables

Add the `MEW_HOSTNAME` environment variable into file `~/.bashrc`
- Necessary for `--last-updated` argument
- Use the hostname for the VM you are working in

```
export MEW_HOSTNAME="linuxvm-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee.ncod.mckinsey.com"
```

---

## Troubleshooting

### Common issues
1. Check your `docs.config.yaml` files are located in the correct directory
2. Check that all fields in the `docs.config.yaml` are inserted correctly. For example: `dir-order` rather than `dir_order`
3. Ensure your filepath references are correct
4. Assets are in the correct `/docs/assets` folder
5. Files and directories referenced in `dir_order`, `dir_details` and `file_order` all exist

---

