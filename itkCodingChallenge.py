#!/usr/bin/env python3

import argparse
import itk
import vtk

parser = argparse.ArgumentParser()
parser.add_argument('inputFileName', type=str,
                    help="name of the input image file ")
#parser.add_argument("output", type=str,
#                    help="name of the output image file ")
args = parser.parse_args()
#print(args.inputFileName)

#reading of the image with itk with a specific pixel type (float)
itkImage = itk.imread(args.inputFileName, itk.F)

#itk smoothing filter applied to image
itkSmooth = itk.anti_alias_binary_image_filter(itkImage, number_of_iterations=4)

# Cast to an unsigned char pixel type
castItkSmooth= itkSmooth.astype(itk.UC)

itk.imwrite(castItkSmooth, "output.tif")

#display the original image and the filtered image in a VTK renderer
# ???


