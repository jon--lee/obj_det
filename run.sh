# Remember to set which CUDA devices to use if you're doing that

# might not have to use these two
python copyfile.py --input_dir rgb  --images_output_dir images --annos_output_dir annotations
python png2jpg.py --dir images

# Convert to csv files and tf records. Automatically does an 80-20 split
python xml_to_csv.py 
python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=data/train.record
python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=data/test.record

# you may cut this next command short if you are done trianing early
# will save training logs and checkouts to ./output
# you may also want to specify which model to start with to finetune. Do that in the config file.
# right now it defaults to the ssd.
CUDA_VISIBLE_DEVICES=1 python ~/models/research/object_detection/train.py \
    --logtostderr \
    --pipeline_config_path=./training/ssd_mobilenet_v1_pets.config \
    --train_dir=./output

# Please set the iteration value for the trained checkpoint file
# Please also specify where the output inference graph should go
# If there is already an output inference graph there, you will have to delete it or rename it.
CUDA_VISIBLE_DEVICES=0 python ~/models/research/object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path training/ssd_mobilenet_v1_pets.config \
    --trained_checkpoint_prefix output/model.ckpt-99 \
    --output_directory models_output/output_inference_graph.pb

