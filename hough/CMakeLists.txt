project(HoughForests)
cmake_minimum_required(VERSION 2.8)

set(CMAKE_BUILD_TYPE Release)

aux_source_directory(. SRC_LIST)
include_directories(/usr/local/include/opencv /usr/local/include/opencv2)
link_directories(/usr/local/lib/)
add_executable(${PROJECT_NAME} ${SRC_LIST})
target_link_libraries( HoughForests ${OpenCV_LIBS})
target_link_libraries(HoughForests
libopencv_calib3d.so
libopencv_contrib.so
libopencv_core.so
libopencv_features2d.so
libopencv_flann.so
libopencv_gpu.so
libopencv_highgui.so
libopencv_imgproc.so
libopencv_legacy.so
libopencv_ml.so
libopencv_nonfree.so
libopencv_objdetect.so
libopencv_ocl.so
libopencv_photo.so
libopencv_stitching.so
libopencv_superres.so
libopencv_ts.so
libopencv_video.so
libopencv_videostab.so
)
