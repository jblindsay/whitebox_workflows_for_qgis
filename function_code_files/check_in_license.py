from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.accumulation_curvature(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.adaptive_filter(raster1, filter_size_x2, filter_size_y3, threshold4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.add_point_coordinates_to_table(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.aggregate_raster(raster1, aggregation_factor2, 'aggregation_type3')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input_raster1')
raster2 = wbe.read_raster('features_raster2')
wbe.anova(raster1, raster2, 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
wbe.ascii_to_las(input_ascii_files1, 'pattern2', epsg_code3)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.aspect(raster1, z_factor2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('routes1')
raster2 = wbe.read_raster('dem2')
outputVector = wbe.assess_route(vector1, raster2, segment_length3, search_radius4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.attribute_correlation(vector1, 'output_html_file2')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.attribute_histogram(vector1, 'field_name2', 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.attribute_scattergram(vector1, 'field_name_x2', 'field_name_y3', 'output_html_file4', add_trendline5)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.average_flowpath_slope(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.average_normal_vector_angular_deviation(raster1, filter_size2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.average_overlay()
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.average_upslope_flowpath_length(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('image1')
outputRaster = wbe.balance_contrast_enhancement(raster1, band_mean2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pntr1')
outputRaster = wbe.basins(raster1, esri_pntr2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.bilateral_filter(raster1, sigma_dist2, sigma_int3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('points1')
raster5 = wbe.read_raster('base_raster5')
outputRaster = wbe.block_maximum(vector1, 'field_name2', use_z3, cell_size4, raster5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('points1')
raster5 = wbe.read_raster('base_raster5')
outputRaster = wbe.block_minimum(vector1, 'field_name2', use_z3, cell_size4, raster5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_and(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_not(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_or(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_xor(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.boundary_shape_complexity(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.breach_depressions_least_cost(raster1, max_cost2, max_dist3, flat_increment4, fill_deps5, minimize_dist6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.breach_single_cell_pits(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputVector = wbe.breakline_mapping(raster1, threshold2, min_length3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.buffer_raster(raster1, buffer_size2, grid_cells_units3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('streams2')
vector3 = wbe.read_vector('roads3')
outputRaster = wbe.burn_streams_at_roads(raster1, vector2, vector3, road_width4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.canny_edge_detection(raster1, sigma2, low_threshold3, high_threshold4, add_back_to_image5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
(outputRaster0, outputString1) = wbe.centroid_raster(raster1)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.centroid_vector(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
(outputRaster0, outputRaster1), outputString2) = wbe.change_vector_analysis()
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.check_in_license('licenseId')
