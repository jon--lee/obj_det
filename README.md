Store images from the labelimg in the rbg folder where xml annotations and pngs/jpegs are in the same folder
with corresponding identifiers (see dataset that was emailed out to the team)

See all usage examples in run.sh


Using copyfile.py copy the images and annotations to their respective folders

Using png2jpg.py convert all images in images/ to jpgs (i think you can skip this step now)

Convert xml files to csvs using xml_to_csv.py which will automatically generate an 80-20 split

Generate tf records of the two csv files using generate_tfrecord.py and passing in input and output paths for train and test respectively

Run the train file from the object_detection repository with paths to your config files (given in this repo) and the output directory.
All training information will be saved in teh output directory including checkpoint files.

Export the graph to a usable inference model using object_detection's expert_inference_graph.py given the config file, the output model checkpoint and the location to put the exported graph

See example flow in run.sh
