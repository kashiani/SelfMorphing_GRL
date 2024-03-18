import os
import numpy as np
import cv2
import locator
import aligner
import warper
import blender
import argparse
from utils import list_img_paths, load_valid_image_points, verify_args, load_image_points, write_file

def morph(src_img, src_points, dest_img, dest_points, width, height, proportion_morphing=0.5):
    """Morph two images."""
    size = (height, width)
    points = locator.weighted_average_points(src_points, dest_points, proportion_morphing)
    src_end = warper.warp_image(src_img, src_points, points, size)
    end_face = warper.warp_image(dest_img, dest_points, points, size)
    average_face_stand = blender.weighted_average(src_end, end_face, proportion_morphing)

    temp_points = points[:-4]
    mask = blender.mask_from_points(size, temp_points)
    mask_src = np.mean(src_end, axis=2) > 0
    mask = np.asarray(mask * mask_src, dtype=np.uint8)

    r = cv2.boundingRect(mask)
    center = (r[0] + int(r[2] / 2), r[1] + int(r[3] / 2))
    average_face_norm = cv2.seamlessClone(average_face_stand, src_end, mask, center, cv2.NORMAL_CLONE)

    return average_face_norm


def morpher(img_paths, width, height, output_dir, proportion_morphing):
    """Morph multiple images."""
    images_points_gen = load_valid_image_points(img_paths, (height, width))
    src_img, src_points = next(images_points_gen)

    for dest_img, dest_points in images_points_gen:

        face_norm = morph(src_img, src_points, dest_img, dest_points,
                          width, height, proportion_morphing)
        write_file(output_dir, proportion_morphing, face_norm)





def main(src, dest, output_dir, proportion_morphing):
    """Main function to initiate morphing."""
    source_face = cv2.imread(src)
    height, width, _ = source_face.shape
    list =  list_img_paths(None, src, dest)
    morpher(list , width, height, output_dir, proportion_morphing)



def process_images_in_directory(input_images, output_dir, proportion_morphing):
    morph_file = []
    for r, d, f in os.walk(input_images):
        for file in f:
            morph_file.append(os.path.join(r, file))

    for i in range(len(morph_file)):
        path_src = morph_file[i].split('/')
        current_img_src = path_src[-1].lower()
        id_src = current_img_src.split('_')[1]
        for j in range(len(morph_file)):
            path_des = morph_file[j].split('/')
            current_img_des = path_des[-1].lower()
            id_des = current_img_des.split('_')[1]
            if id_src != id_des or morph_file[i] == morph_file[j]:
                continue
            output_directory = os.path.join(output_dir, morph_file[i].split('/')[-1][:-4] + "_" + morph_file[j].split('/')[-1])

            if not os.path.exists(output_directory):
                try:
                    main(morph_file[i], morph_file[j], output_directory, proportion_morphing)
                except:
                    print("Failed")
                    continue



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Morph images')
    parser.add_argument('--source_images', type=str, help='Path to folder containing images', default ='./src_images/FERET_MTCNN')
    parser.add_argument('--output', type=str, help='Path to output folder', default ='./out_images/self_FERET')
    parser.add_argument('--proportion_morphing', type=float, default=0.5, help='Proportion of morphing two input images.')
    args = parser.parse_args()
    process_images_in_directory(args.source_images, args.output, args.proportion_morphing)


