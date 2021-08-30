#!/usr/bin/env python3

import argparse
import itk
#import vtk

def smoothing(): #error
  # Cast to a float pixel type 
  itkCastImage = itkImage.astype(itk.D)
  #itk smoothing filter applied to image
  itkSmooth = itk.anti_alias_binary_image_filter(itkImage, number_of_iterations=4)

  itk.imwrite(itkSmooth, "output.png")

def median(): #ok
  itkMedian = itk.median_image_filter(itkImage, radius=2)
  itk.imwrite(itkMedian, "output.png")


parser = argparse.ArgumentParser()
parser.add_argument('inputFileName', type=str,
                    help="name of the input image file ")
args = parser.parse_args()


#reading of the image with itk with a specific pixel type (unsigned char)
itkImage = itk.imread(args.inputFileName, itk.UC)

smoothing()

#display the original image and the filtered image in a VTK renderer


###################################################################################

# Read the original image
image1_reader = vtk.vtkPNGReader()
image1_reader.SetFileName(args.inputFileName)
image1_reader.Update()
image1_data = image1_reader.GetOutput()
# Create an image actor to display the image
image1_actor = vtk.vtkImageActor()
image1_actor.SetInputData(image1_data)
# Create a renderer to display the original image
original_renderer = vtk.vtkRenderer()
original_renderer.AddActor(image1_actor)
original_renderer.SetViewport(0.0, 0.0, 0.5, 1.0)

# ??? unsure if that's necessary
# Render once to figure out where the background camera will be
render_window.Render()
# Set up the background camera to fill the renderer with the image
origin1 = image1_data.GetOrigin()
spacing1 = image1_data.GetSpacing()
extent1 = image1_data.GetExtent()
camera1 = background_renderer.GetActiveCamera()
camera1.ParallelProjectionOn()

# Read the filtered image
image2_reader = vtk.vtkPNGReader()
image2_reader.SetFileName("output.png")
image2_reader.Update()
image2_data = image2_reader.GetOutput()
# Create an image actor to display the image
image2_actor = vtk.vtkImageActor()
image2_actor.SetInputData(image2_data)
# Create a renderer to display the filtered image
filtered_renderer = vtk.vtkRenderer()
filtered_renderer.AddActor(image2_actor)
filtered_renderer.SetViewport(0.5, 0.0, 1.0, 1.0)

# ??? unsure if that's necessary
# Render once to figure out where the background camera will be
render_window.Render()
# Set up the background camera to fill the renderer with the image
origin2 = image1_data.GetOrigin()
spacing2 = image1_data.GetSpacing()
extent2 = image1_data.GetExtent()
camera2 = background_renderer.GetActiveCamera()
camera2.ParallelProjectionOn()

filtered_renderer.SetViewport(0.5, 0.0, 1.0, 1.0)
# Create the render window which will show up on the screen.
# We put our renderer into the render window using AddRenderer. We also
# set the size to be 300 pixels by 300.

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(original_renderer)
renWin.AddRenderer(filtered_renderer)
renWin.SetSize(600, 300)
renWin.SetWindowName("Original and filtered image")

renWin.Render()