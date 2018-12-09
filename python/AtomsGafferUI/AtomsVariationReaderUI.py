##########################################################################
#
#  Copyright (c) 2018, Toolchefs Ltd. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import IECore

import Gaffer
import AtomsGaffer

import DocumentationAlgo

Gaffer.Metadata.registerNode(

    AtomsGaffer.AtomsVariationReader,

    "description",
    """
    Loads Atoms Agent variations in a default pose.
    """,

    "icon", "atoms_logo.png",
    "documentation:url", DocumentationAlgo.documentationURL,

    plugs = {

        "atomsVariationFile" : [

            "description",
            """
            The full path to an Atoms variation file.
            """,

            "plugValueWidget:type", "GafferUI.FileSystemPathPlugValueWidget",
            "path:leaf", True,
            "path:valid", True,
            "path:bookmarks", "atoms",
            "fileSystemPath:extensions", "json",
            "fileSystemPath:extensionsLabel", "Show only Json files",
            "layout:index", 0,

        ],

        "Pref" : [

            "description",
            """
            Generate Pref prim var
            """,
            "layout:section", "Polygon options",
        ],

        "Nref" : [

            "description",
            """
            Generate Nref prim var
            """,
            "layout:section", "Polygon options",
        ],

        "refreshCount" : [

            "description",
            """
            May be incremented to force a reload if the file has
			changed on disk - otherwise old contents may still
			be loaded via Gaffer's cache.
            """,

            "plugValueWidget:type", "GafferUI.RefreshPlugValueWidget",
            "layout:label", "",
            "layout:accessory", True,
            "layout:index", 1,
        ],

    },

)
