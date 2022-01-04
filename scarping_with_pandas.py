#!/bin/bash 

#work with html tables

conda install -c anaconda pandas
conda install -c anaconda lxml
jupyter

  import pandas as pd
  import ssl
  ssl._create_default_https_context=ssl._create_unverfied_context
  scarper= pd.read_html("url")
  for index, table in enumerate(scarper):
      print("*********************************************************")
      print(index)
      print(table)
  
  scarper[3]
