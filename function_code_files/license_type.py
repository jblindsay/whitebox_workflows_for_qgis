from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.accumulation_curvature(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.adaptive_filter(raster1, filter_size_x2, filter_size_y3, threshold4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.add_point_coordinates_to_table(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.aggregate_raster(raster1, aggregation_factor2, 'aggregation_type3')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input_raster1')
raster2 = wbe.read_raster('features_raster2')
wbe.anova(raster1, raster2, 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
wbe.ascii_to_las(input_ascii_files1, 'pattern2', epsg_code3)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.aspect(raster1, z_factor2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('routes1')
raster2 = wbe.read_raster('dem2')
outputVector = wbe.assess_route(vector1, raster2, segment_length3, search_radius4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.attribute_correlation(vector1, 'output_html_file2')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.attribute_histogram(vector1, 'field_name2', 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.attribute_scattergram(vector1, 'field_name_x2', 'field_name_y3', 'output_html_file4', add_trendline5)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.average_flowpath_slope(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.average_normal_vector_angular_deviation(raster1, filter_size2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.average_overlay()
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.average_upslope_flowpath_length(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('image1')
outputRaster = wbe.balance_contrast_enhancement(raster1, band_mean2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pntr1')
outputRaster = wbe.basins(raster1, esri_pntr2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.bilateral_filter(raster1, sigma_dist2, sigma_int3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('points1')
raster5 = wbe.read_raster('base_raster5')
outputRaster = wbe.block_maximum(vector1, 'field_name2', use_z3, cell_size4, raster5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('points1')
raster5 = wbe.read_raster('base_raster5')
outputRaster = wbe.block_minimum(vector1, 'field_name2', use_z3, cell_size4, raster5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_and(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_not(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_or(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input11')
raster2 = wbe.read_raster('input22')
outputRaster = wbe.bool_xor(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.boundary_shape_complexity(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.breach_depressions_least_cost(raster1, max_cost2, max_dist3, flat_increment4, fill_deps5, minimize_dist6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.breach_single_cell_pits(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputVector = wbe.breakline_mapping(raster1, threshold2, min_length3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.buffer_raster(raster1, buffer_size2, grid_cells_units3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('streams2')
vector3 = wbe.read_vector('roads3')
outputRaster = wbe.burn_streams_at_roads(raster1, vector2, vector3, road_width4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.canny_edge_detection(raster1, sigma2, low_threshold3, high_threshold4, add_back_to_image5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
(outputRaster0, outputString1) = wbe.centroid_raster(raster1)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.centroid_vector(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
(outputRaster0, outputRaster1), outputString2) = wbe.change_vector_analysis()
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.circular_variance_of_aspect(raster1, filter_size2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('in_lidar1')
vector2 = wbe.read_vector('building_footprints2')
outpuLidar = wbe.classify_buildings_in_lidar(lidar1, vector2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
outpuLidar = wbe.classify_lidar(lidar1, search_radius2, grd_threshold3, oto_threshold4, linearity_threshold5, planarity_threshold6, num_iter7, facade_threshold8)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
outpuLidar = wbe.colourize_based_on_class(lidar1, intensity_blending_amount2, 'clr_str3', use_unique_clrs_for_buildings4, search_radius5)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
outpuLidar = wbe.colourize_based_on_point_returns(lidar1, intensity_blending_amount2, 'only_ret_colour3', 'first_ret_colour4', 'intermediate_ret_colour5', 'last_ret_colour6')
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('in_lidar1')
outpuLidar = wbe.classify_overlap_points(lidar1, resolution2, 'overlap_criterion3', filter4)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.clean_vector(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
vector2 = wbe.read_vector('clip_layer2')
outputVector = wbe.clip(vector1, vector2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input1')
vector2 = wbe.read_vector('polygons2')
outpuLidar = wbe.clip_lidar_to_polygon(lidar1, vector2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
vector2 = wbe.read_vector('polygons2')
outputRaster = wbe.clip_raster_to_polygon(raster1, vector2, maintain_dimensions3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.closing(raster1, filter_size_x2, filter_size_y3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.clump(raster1, diag2, zero_background3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.compactness_ratio(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.conservative_smoothing_filter(raster1, filter_size_x2, filter_size_y3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input_points1')
outputVector = wbe.construct_vector_tin(vector1, 'field_name2', use_z3, max_triangle_edge_length4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.contours_from_points(vector1, 'field_name2', use_z_values3, max_triangle_edge_length4, contour_interval5, base_contour6, smoothing_filter_size7)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('raster_surface1')
outputVector = wbe.contours_from_raster(raster1, contour_interval2, base_contour3, smoothing_filter_size4, deflection_tolerance5)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.convert_nodata_to_zero(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.corner_detection(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('image1')
vector2 = wbe.read_vector('principal_point2')
outputRaster = wbe.correct_vignetting(raster1, vector2, focal_length3, image_width4, n_param5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('source1')
raster2 = wbe.read_raster('backlink2')
outputRaster = wbe.cost_allocation(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('source1')
raster2 = wbe.read_raster('cost2')
(outputRaster0, outputRaster1) = wbe.cost_distance(raster1, raster2)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('destination1')
raster2 = wbe.read_raster('backlink2')
outputRaster = wbe.cost_pathway(raster1, raster2, zero_background3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.count_if(, comparison_value2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('red1')
raster2 = wbe.read_raster('green2')
raster3 = wbe.read_raster('blue3')
raster4 = wbe.read_raster('opacity4')
outputRaster = wbe.create_colour_composite(raster1, raster2, raster3, raster4, enhance5, treat_zeros_as_nodata6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('base_file1')
outputRaster = wbe.create_plane(raster1, gradient2, aspect3, constant4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
wbe.crispness_index(raster1, 'output_html_file2')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('raster11')
raster2 = wbe.read_raster('raster22')
wbe.cross_tabulation(raster1, raster2, 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputVector = wbe.csv_points_to_vector('input_file1', x_field_num2, y_field_num3, epsg4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.cumulative_distribution(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.curvedness(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.d8_flow_accum(raster1, 'out_type2', log_transform3, clip4, input_is_pointer5, esri_pntr6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('loading2')
raster3 = wbe.read_raster('efficiency3')
raster4 = wbe.read_raster('absorption4')
outputRaster = wbe.d8_mass_flux(raster1, raster2, raster3, raster4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.d8_pointer(raster1, esri_pointer2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.dbscan(, 'scaling_method2', search_distance3, min_points4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('fill2')
outputRaster = wbe.dem_void_filling(raster1, raster2, mean_plane_dist3, 'edge_treatment4', weight_value5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.depth_in_sink(raster1, zero_background2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('streams2')
vector3 = wbe.read_vector('lakes3')
outputRaster = wbe.depth_to_water(raster1, vector2, vector3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.deviation_from_mean_elevation(raster1, filter_size_x2, filter_size_y3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.deviation_from_regional_direction(vector1, elongation_threshold2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.diff_of_gaussians_filter(raster1, sigma12, sigma23)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
vector2 = wbe.read_vector('overlay2')
outputVector = wbe.difference(vector1, vector2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.difference_curvature(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.difference_from_mean_elevation(raster1, filter_size_x2, filter_size_y3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.dinf_flow_accum(raster1, 'out_type2', convergence_threshold3, log_transform4, clip5, input_is_pointer6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('loading2')
raster3 = wbe.read_raster('efficiency3')
raster4 = wbe.read_raster('absorption4')
outputRaster = wbe.dinf_mass_flux(raster1, raster2, raster3, raster4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.dinf_pointer(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('image1')
outputRaster = wbe.direct_decorrelation_stretch(raster1, achromatic_factor2, clip_percent3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.directional_relief(raster1, azimuth2, max_dist3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.dissolve(vector1, 'dissolve_field2', snap_tolerance3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pointer1')
raster2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.distance_to_outlet(raster1, raster2, esri_pointer3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.diversity_filter(raster1, filter_size_x2, filter_size_y3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('streams2')
outputRaster = wbe.downslope_distance_to_stream(raster1, raster2, use_dinf3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pointer1')
raster2 = wbe.read_raster('watersheds2')
raster3 = wbe.read_raster('weights3')
outputRaster = wbe.downslope_flowpath_length(raster1, raster2, raster3, esri_pntr4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.downslope_index(raster1, vertical_drop2, 'output_type3')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.edge_contamination(raster1, 'flow_type2', z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.edge_density(raster1, filter_size2, normal_diff_threshold3, z_factor4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.edge_preserving_mean_filter(raster1, filter_size2, threshold3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
(outputRaster0, outputString1) = wbe.edge_proportion(raster1)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.elev_relative_to_min_max(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('watersheds2')
outputRaster = wbe.elev_relative_to_watershed_min_max(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.elevation_above_pit(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('streams2')
outputRaster = wbe.elevation_above_stream(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
raster2 = wbe.read_raster('streams2')
outputRaster = wbe.elevation_above_stream_euclidean(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.elevation_percentile(raster1, filter_size_x2, filter_size_y3, sig_digits4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.eliminate_coincident_points(vector1, tolerance_dist2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.elongation_ratio(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('roads_vector2')
(outputRaster0 = wbe.embankment_mapping(raster1, vector2, search_dist3, min_road_width4, typical_embankment_width5, typical_embankment_max_height6, embankment_max_width7, max_upwards_increment8, spillout_slope9, remove_embankments10)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.emboss_filter(raster1, 'direction2', clip_amount3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
vector2 = wbe.read_vector('erase_layer2')
outputVector = wbe.erase(vector1, vector2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input1')
vector2 = wbe.read_vector('polygons2')
outpuLidar = wbe.erase_polygon_from_lidar(lidar1, vector2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
vector2 = wbe.read_vector('polygons2')
outputRaster = wbe.erase_polygon_from_raster(raster1, vector2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.euclidean_allocation(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.euclidean_distance(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector2 = wbe.read_vector('training_polygons2')
wbe.evaluate_training_sites(, vector2, 'class_field_name3', 'output_html_file4')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
wbe.export_table_to_csv(vector1, 'output_csv_file2', headers3)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.exposure_towards_wind_flux(raster1, azimuth2, max_dist3, z_factor4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.extend_vector_lines(vector1, distance2, 'extend_direction3')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.extract_by_attribute(vector1, 'statement2')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.extract_nodes(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector2 = wbe.read_vector('points2')
(outputVector0, outputString1) = wbe.extract_raster_values_at_points(, vector2)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('flow_accumulation1')
outputRaster = wbe.extract_streams(raster1, threshold2, zero_background3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.extract_valleys(raster1, 'variant2', line_thin3, filter_size4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pointer1')
raster2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.farthest_channel_head(raster1, raster2, esri_pointer3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.fast_almost_gaussian_filter(raster1, sigma2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fd8_flow_accum(raster1, 'out_type2', exponent3, convergence_threshold4, log_transform5, clip6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fd8_pointer(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.feature_preserving_smoothing(raster1, filter_size2, normal_diff_threshold3, iterations4, max_elevation_diff5, z_factor6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fetch_analysis(raster1, azimuth2, height_increment3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('streams2')
outputRaster = wbe.fill_burn(raster1, vector2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fill_depressions(raster1, fix_flats2, flat_increment3, max_depth4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fill_depressions_planchon_and_darboux(raster1, fix_flats2, flat_increment3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fill_depressions_wang_and_liu(raster1, fix_flats2, flat_increment3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fill_missing_data(raster1, filter_size2, weight3, exclude_edge_nodata4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.fill_pits(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar2 = wbe.read_lidar('input_lidar2')
outpuLidar = wbe.filter_lidar('statement1', lidar2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input1')
outpuLidar = wbe.filter_lidar_classes(lidar1, exclusion_classes2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('in_lidar1')
outpuLidar = wbe.filter_lidar_scan_angles(lidar1, threshold2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputRaster = wbe.filter_raster_features_by_area(raster1, threshold2, zero_background3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('in_lidar1')
outpuLidar = wbe.find_flightline_edge_points(lidar1)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputVector = wbe.find_lowest_or_highest_points(raster1, 'output_type2')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pointer1')
raster2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.find_main_stem(raster1, raster2, esri_pointer3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.find_noflow_cells(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pntr1')
raster2 = wbe.read_raster('streams2')
outputRaster = wbe.find_parallel_flow(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.find_patch_edge_cells(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.find_ridges(raster1, line_thin2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.fix_dangling_arcs(vector1, snap_dist2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('lakes2')
outputRaster = wbe.flatten_lakes(raster1, vector2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
outputRaster = wbe.flightline_overlap(lidar1, resolution2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.flip_image(raster1, 'direction2')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.flood_order(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
(outputRaster0, outputRaster1), outputRaster2) = wbe.flow_accum_full_workflow(raster1, 'out_type2', log_transform3, clip4, esri_pntr5)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.write_raster(outputRaster2, 'fnOutput2', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pointer1')
outputRaster = wbe.flow_length_diff(raster1, esri_pointer2, log_transform3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.gamma_correction(raster1, gamma_value2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.gaussian_contrast_stretch(raster1, num_tones2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.gaussian_curvature(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.gaussian_filter(raster1, sigma2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.geomorphons(raster1, search_distance2, flatness_threshold3, flatness_distance4, skip_distance5, output_forms6, analyze_residuals7)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.generalize_classified_raster(raster1, area_threshold2, 'method3')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.generalize_with_similarity(raster1, area_threshold3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.generating_function(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pntr1')
raster2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.hack_stream_order(raster1, raster2, esri_pntr3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('points1')
raster5 = wbe.read_raster('base_raster5')
outputRaster = wbe.heat_map(vector1, 'field_name2', bandwidth3, cell_size4, raster5, 'kernel_function6')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input1')
outpuLidar = wbe.height_above_ground(lidar1)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('base1')
outputVector = wbe.hexagonal_grid_from_raster_base(raster1, width2, 'orientation3')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('base1')
outputVector = wbe.hexagonal_grid_from_vector_base(vector1, width2, 'orientation3')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.high_pass_filter(raster1, filter_size_x2, filter_size_y3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.high_pass_median_filter(raster1, filter_size_x2, filter_size_y3, sig_digits4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.highest_position()
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.hillshade(raster1, azimuth2, altitude3, z_factor4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pntr1')
raster2 = wbe.read_raster('streams2')
outputRaster = wbe.hillslopes(raster1, raster2, esri_pntr3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.histogram_equalization(raster1, num_tones2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('image1')
outputRaster = wbe.histogram_matching(raster1, histogram2, histo_is_cumulative3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('image11')
raster2 = wbe.read_raster('image22')
outputRaster = wbe.histogram_matching_two_images(raster1, raster2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.hole_proportion(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.horizon_angle(raster1, azimuth2, max_dist3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.horizontal_excess_curvature(raster1, log_transform2, z_factor3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pntr1')
raster2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.horton_stream_order(raster1, raster2, esri_pntr3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
(outputRaster0, outputRaster1) = wbe.hydrologic_connectivity(raster1, exponent2, convergence_threshold3, z_factor4)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
wbe.hypsometric_analysis(, 'output_html_file2')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.hypsometrically_tinted_hillshade(raster1, solar_altitude2, hillshade_weight3, brightness4, atmospheric_effects5, 'palette6', reverse_palette7, full_360_mode8, z_factor9)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('points1')
raster8 = wbe.read_raster('base_raster8')
outputRaster = wbe.idw_interpolation(vector1, 'field_name2', use_z3, weight4, radius5, min_points6, cell_size7, raster8)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('intensity1')
raster2 = wbe.read_raster('hue2')
raster3 = wbe.read_raster('saturation3')
(outputRaster0, outputRaster1), outputRaster2) = wbe.ihs_to_rgb(raster1, raster2, raster3)
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.write_raster(outputRaster2, 'fnOutput2', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
wbe.image_autocorrelation(, 'output_html_file2', 'contiguity_type3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
wbe.image_correlation(, 'output_html_file2')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('raster11')
raster2 = wbe.read_raster('raster22')
(outputRaster0, outputRaster1) = wbe.image_correlation_neighbourhood_analysis(raster1, raster2, filter_size3, 'correlation_stat4')
wbe.write_raster(outputRaster0, 'fnOutput0', compressRaster)
wbe.write_raster(outputRaster1, 'fnOutput1', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('independent_variable1')
raster2 = wbe.read_raster('dependent_variable2')
outputRaster = wbe.image_regression(raster1, raster2, 'output_html_file3', standardize_residuals4, output_scattergram5, num_samples6)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.image_segmentation(, dist_threshold2, num_steps3, area_threshold4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment, WbPalette, WbPalette
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('left_raster1')
raster2 = wbe.read_raster('right_raster2')
wbe.image_slider(raster1, raster2, 'output_html_file3', left_palette4, left_reverse_palette5, 'left_label6', right_palette7, right_reverse_palette8, 'right_label9', image_height10)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector2 = wbe.read_vector('points2')
wbe.image_stack_profile(, vector2, 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
( = wbe.impoundment_size_index(raster1, max_dam_length2, output_mean3, output_max4, output_volume5, output_area6, output_height7)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
outputVector = wbe.individual_tree_detection(lidar1, min_search_radius2, min_height3, max_search_radius4, max_height5, only_use_veg6)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
vector2 = wbe.read_vector('dam_points2')
outputRaster = wbe.insert_dams(raster1, vector2, dam_length3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('dem1')
outputRaster = wbe.isobasins(raster1, target_size2, connections3, 'csv_file4')
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.integral_image_transform(raster1)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
vector2 = wbe.read_vector('overlay2')
outputVector = wbe.intersect(vector1, vector2, snap_tolerance3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('pour_pts1')
raster2 = wbe.read_raster('streams2')
outputVector = wbe.jenson_snap_pour_points(vector1, raster2, snap_dist3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('primary_vector1')
vector3 = wbe.read_vector('foreign_vector3')
wbe.join_tables(vector1, 'primary_key_field2', vector3, 'foreign_key_field4', 'import_field5')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
outputRaster = wbe.k_means_clustering(, 'output_html_file2', num_clusters3, max_iterations4, percent_changed_threshold5, 'initialization_mode6', min_class_size7)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.k_nearest_mean_filter(raster1, filter_size_x2, filter_size_y3, k4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('class_raster1')
raster2 = wbe.read_raster('reference_raster2')
wbe.kappa_index(raster1, raster2, 'output_html_file3')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector2 = wbe.read_vector('training_data2')
outputRaster = wbe.knn_classification(, vector2, 'class_field_name3', 'scaling_method4', k5, test_proportion6, use_clipping7, create_output8)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector2 = wbe.read_vector('training_data2')
outputRaster = wbe.knn_regression(, vector2, 'field_name3', 'scaling_method4', k5, distance_weighting6, test_proportion7, create_output8)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
wbe.ks_normality_test(raster1, 'output_html_file2', num_samples3)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.laplacian_filter(raster1, 'variant2', clip_amount3)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.laplacian_of_gaussians_filter(raster1, sigma2)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
wbe.las_to_ascii(lidar1)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
lidar1 = wbe.read_lidar('input_lidar1')
outputVector = wbe.las_to_shapefile(lidar1, output_multipoint2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('input1')
outputVector = wbe.layer_footprint_raster(raster1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
vector1 = wbe.read_vector('input1')
outputVector = wbe.layer_footprint_vector(vector1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('inputRaster1')
outputRaster = wbe.lee_filter(raster1, filter_size_x2, filter_size_y3, sigma4, m_value5)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('licenseId')
wbe.verbose = True
raster1 = wbe.read_raster('d8_pointer1')
raster2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.length_of_upstream_channels(raster1, raster2, esri_pointer3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compressRaster)
wbe.check_in_license('licenseId')
