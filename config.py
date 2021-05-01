import os

threshold=0.5
bin_width=10

path_prefix='data'
manually_segmented_path=os.path.join(path_prefix, 'manually_labels')
dissected_path=os.path.join(path_prefix, 'dissected')
output_path=os.path.join(path_prefix, 'training')
mld_features_path=os.path.join(path_prefix, 'mld_training_features-%d-%f.csv' % (bin_width, threshold))
hinds_features_path=os.path.join(path_prefix, 'hinds_training_features-%d-%f.csv' % (bin_width, threshold))
xls_path= os.path.join(path_prefix, '06_20180109-CT-cut.xlsx')

save_registered_images=True

os.makedirs(output_path, exist_ok=True)
