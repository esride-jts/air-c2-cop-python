# -*- coding: utf-8 -*-

###############################################################################
# Authors: Jan Tschada, Esri Deutschland GmbH, Nov 2019
# It is much more of an automated use case scenario.
# The following environment variables must be defined:
# %aco_feature_class%
# %aco_elevation_source%
# %aco_output_workspace%
# The air control order features must exists in a geodatabase.
# The elevation raster must exists in a geodatabase.
# The output workspace e.g. file geodatabase must exists.
###############################################################################

import os
import sys
import unittest

import arcpy
arcpy.env.overwriteOutput = True

class TestCreate3dAirControlOrder(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCreate3dAirControlOrder, self).__init__(*args, **kwargs)
        self._aco_feature_class = os.environ["aco_feature_class"]
        self._aco_elevation_source = os.environ["aco_elevation_source"]
        self._aco_output_workspace = os.environ["aco_output_workspace"]
        sys.argv.append(self._aco_feature_class)
        sys.argv.append(self._aco_elevation_source)
        sys.argv.append(self._aco_output_workspace)

    def test_create_3d(self):
        from airspacemanagement import create3DACO
        self._aco_multipatch_class = "%s/AirC2_ACO_POLYGON_3D" % (self._aco_output_workspace)
        self.assertEqual(arcpy.GetCount_management(self._aco_feature_class), arcpy.GetCount_management(self._aco_multipatch_class), "The feature count must match!")

if __name__ == "__main__":
    unittest.main()