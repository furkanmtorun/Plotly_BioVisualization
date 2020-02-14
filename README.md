  
# Plotly BioVisualization with Python

## :hash: What is the purpose of this repo?
Tremendous advances in the field of biotechnology enable researchers and scientists to produce and obtain a diverse and huge amount of biological data.  Therefore, there is a corresponding increase in the way of visualizing the biological data to represent information and science through art in a concise and meaningful way. 

In this respect, [Plotly](https://plot.ly/) has recently emerged and it can be used to create interactive charts and state-of-the-art graphs in a wide range of visualization applications including visualization of sequences, genomes, alignments, gene expressions. 

So, I have wanted to learn how to use this library with Python, create some great charts and shared them. 

## :hash: How it looks like in general?
![Plotly_BioVis_Gif](https://github.com/furkanmtorun/Plotly_BioVisualization/raw/master/Plotly_BioVisualization.gif)


## :hash: Requirements and Installation
 - Create a directory and download all files or clone the repository via Git using the following command:
 
 	`git clone https://github.com/furkanmtorun/Plotly_BioVisualization.git`

 - Install the required packages if you do not already:
 
	` pip install -r requirements.txt `

- Then, the turn to run it: 

	`python Plotly_BioVisualization.py`

- It's ready to use now! Open your web browser and go to:

	`http://127.0.0.1:8050 `

> If you did not install **pip** yet, please follow the instruction [here](https://pip.pypa.io/en/stable/installing/).

> In the development process, Python 3 has been used. The use of Python 2.x might cause compatibility issues.  

## :hash: How to create interactive graphs and charts?

- ### :hash:  Needle Plot
	- **Purpose:** It allows you to illustrate the mutations or other changes on the corresponding positions of amino acids within the protein sequence together with the protein domains.
	- **Data structure:** JSON / Dict = `{ x: [], y: [], domains: [], mutationGroups: [] }`
	
		![Needle Plot Data](https://user-images.githubusercontent.com/49681382/74552773-086fec80-4f67-11ea-86ae-44b845a5c5a2.png)
	
	- **Coding (just review the code, the comments are over there!):**

		![Needle Plot Code](https://user-images.githubusercontent.com/49681382/74553656-dcee0180-4f68-11ea-88ec-99b9f12a5a47.png)

	- **How it looks like?:**
	![Needle Plot](https://user-images.githubusercontent.com/49681382/74552991-71effb00-4f67-11ea-91c3-8e4ac9a8ddf2.png)


- ### :hash:  Sequence/Alignment Viewer
	- **Purpose:** It allows you to visualize the genomics and transcriptomic sequence with several features such as coverage, gaps, consensus, and heatmap overview.
	- **Data Structure:** FASTA / Clustal
			![Seq. Data](https://user-images.githubusercontent.com/49681382/74554009-951baa00-4f69-11ea-9faf-b94b481ce4e5.png)
	
	- **Coding (just review the code, the comments are over there!):**
		![Seq. Coding](https://user-images.githubusercontent.com/49681382/74554436-9ef1dd00-4f6a-11ea-9eaa-8dcaf9b206da.png)	

	- **How it looks like?**
		![Seq. Viewer](https://user-images.githubusercontent.com/49681382/74554313-50444300-4f6a-11ea-8fa2-645a625413eb.png)

- ### :hash:  Manhattan Plot
	- **Purpose:** Manhattan Plot is a type of scatter plot and commonly used in genome-wide association studies (GWAS) to visualize display significant SNPs efficiently.
		> The genome-wide significance threshold was set as 5e-8 and plotted with green line, and the most significant SNPs are colored in red.
	- **Coding (just review the code, the comments are over there!):**
			![MP-Coding](https://user-images.githubusercontent.com/49681382/74554893-96e66d00-4f6b-11ea-98a1-55a79fd02c1a.png)

	- **How it looks like?**
	
		![MPlot](https://user-images.githubusercontent.com/49681382/74554587-f2642b00-4f6a-11ea-8a1e-83a12b4ab742.png)




## :hash: Sources & References

 - Hossain, S. (2019). Visualization of Bioinformatics Data with Dash Bio. Proceedings of the 18th Python in Science Conference. doi: 10.25080/majora-7ddc1dd1-012.
  - Plotly Dash Bio  Announcement Blog Post: [https://medium.com/plotly/announcing-dash-bio-ed8835d5da0c](https://medium.com/plotly/announcing-dash-bio-ed8835d5da0c)
 - Plotly Dash Bio Page: [https://dash.plot.ly/dash-bio](https://dash.plot.ly/dash-bio)
	 - Alignment Chart Details: [https://dash.plot.ly/dash-bio/alignmentchart](https://dash.plot.ly/dash-bio/alignmentchart)
	 - Manhattan Plot Details: https://dash.plot.ly/dash-bio/manhattanplot
	 - Needle Plot Details: https://dash.plot.ly/dash-bio/needleplot
 - Plotly Bioinformatics Notebook: [https://plot.ly/python/v3/ipython-notebooks/bioinformatics/](https://plot.ly/python/v3/ipython-notebooks/bioinformatics/)
 - Plotly HTML Components Page: [https://dash.plot.ly/dash-html-components](https://dash.plot.ly/dash-html-components) 
 - Bulma.css Documentation: [https://bulma.io/documentation/](https://bulma.io/documentation/)
 - Create and share beautiful screenshots: [https://carbon.now.sh/](https://carbon.now.sh/) 

> Thanks for all these resources!

## :hash: Contributing & Feedback
**I would be very happy to see any feedback and contributions on the repository.**
> I will keep continuing to append new interactive graphs and figures as much as I can.


**Furkan Torun — [furkanmtorun@gmail.com](mailto:furkanmtorun@gmail.com)** 

Twitter: [@furkanmtorun](https://twitter.com/furkanmtorun) 

Website: [furkanmtorun.github.io](https://furkanmtorun.github.io/)

Academics: [Google Scholar Profile](https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ)
