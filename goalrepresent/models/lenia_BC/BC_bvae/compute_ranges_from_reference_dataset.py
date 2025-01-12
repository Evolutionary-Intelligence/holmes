import numpy as np
from BC_bvae import BCBVAE

from goalrepresent.datasets.image.imagedataset import LENIADataset
from goalrepresent.helper.randomhelper import set_seed

if __name__ == '__main__':

    set_seed(0)

    # load reference dataset
    dataset_config = LENIADataset.default_config()
    dataset_config.data_root = '/gpfswork/rech/zaj/ucf28eq/data/lenia_datasets/data_005/'
    dataset_config.split = 'train'
    dataset = LENIADataset(config=dataset_config)

    # load model
    bc_bvae = BCBVAE(set_BC_range=False)

    z_values = np.zeros((dataset.n_images, bc_bvae.n_latents))
    for idx in range(dataset.n_images):
        im = dataset.get_image(idx).squeeze().numpy()
        cur_z = bc_bvae.calc_embedding(im)
        z_values[idx] = cur_z

    np.savez('reference_dataset_bvae_descriptors_values.npz', z=z_values)

    np.savez('reference_dataset_bvae_descriptors_range.npz',
             low=np.percentile(z_values, 0.01, axis=0), high=np.percentile(z_values, 99.9, axis=0))

