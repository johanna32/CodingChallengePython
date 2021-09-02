#!/usr/bin/env python3

import argparse
import itk
import vtk

def main():
  #read the arguments with argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('inputFileName', type=str, 
    help="name of the input image file ")
  parser.add_argument('outputFileName', type=str, 
    help="name of the output file")
  parser.add_argument('r', type=int,
    help="radius of the median filter")
  args = parser.parse_args()


  #reading of the image with itk with a specific pixel type (unsigned char)
  itkImage = itk.imread(args.inputFileName, itk.UC)

  #applt median filter to the image
  itkMedian = itk.median_image_filter(itkImage, radius=args.r)
  itk.imwrite(itkMedian, args.outputFileName)

  #display the original image and the filtered image in a VTK renderer

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

  # Read the filtered image
  image2_reader = vtk.vtkPNGReader()
  image2_reader.SetFileName(args.outputFileName)
  image2_reader.Update()
  image2_data = image2_reader.GetOutput()
  # Create an image actor to display the image
  image2_actor = vtk.vtkImageActor()
  image2_actor.SetInputData(image2_data)
  # Create a renderer to display the filtered image
  filtered_renderer = vtk.vtkRenderer()
  filtered_renderer.AddActor(image2_actor)
  filtered_renderer.SetViewport(0.5, 0.0, 1.0, 1.0)

  # Create the render window which will show up on the screen.
  # We put our renderer into the render window using AddRenderer. We also
  # set the size to be 300 pixels by 300.

  renWin = vtk.vtkRenderWindow()
  renWin.AddRenderer(original_renderer)
  renWin.AddRenderer(filtered_renderer)
  renWin.SetSize(600, 300)
  renWin.SetWindowName("Original and filtered image")



  render_window_interactor = vtk.vtkRenderWindowInteractor()
  render_window_interactor.SetRenderWindow(renWin)
  render_window_interactor.Start()


if __name__ == '__main__':
  main()