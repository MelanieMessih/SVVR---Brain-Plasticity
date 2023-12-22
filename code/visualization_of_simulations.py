# state file generated using paraview version 5.12.0-RC1
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2106, 1390]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [94.10973930358887, 71.95840525627136, 80.29355025291443]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [148.45050505397498, -346.480957069016, 146.6036281304517]
renderView1.CameraFocalPoint = [94.1097393035876, 71.95840525627207, 80.29355025291444]
renderView1.CameraViewUp = [-0.3585671535684529, 0.10050699048061332, 0.9280775513104211]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 133.7652645472802
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(2106, 1390)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the selections
# ----------------------------------------------------------------

# create a new 'Frustum Selection Source'
selection_sources28001 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.28001', FieldType='POINT',
    Frustum=[178.67537104022662, -107.92995120946098, -75.87956597683267, 1.0, 10.191213738226148, 193.91582283399515, 374.65819279980343, 1.0, 178.55669774255034, -115.9289296215279, -69.29205620042443, 1.0, 9.902890298168849, 174.48185564954585, 390.66291768177456, 1.0, 195.45894105201972, -104.5506984395247, -71.47390548587516, 1.0, 50.96783945771126, 202.12590717924493, 385.36199233474554, 1.0, 195.34026775434344, -112.54967685159163, -64.88639570946691, 1.0, 50.67951601765396, 182.69193999479558, 401.3667172167165, 1.0])

# create a new 'Frustum Selection Source'
selection_sources27162 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.27162', FieldType='POINT',
    Frustum=[95.24303284339405, -85.84872685764208, 140.7761252629414, 1.0, 157.57869943625212, 270.4200229674249, -49.02614313910168, 1.0, 92.99255592376953, -83.85814097769783, 144.51983871799538, 1.0, 151.79560313725293, 275.5352719774288, -39.40584655323472, 1.0, 99.63657661493906, -85.20537205105155, 143.07515694973077, 1.0, 168.8688781993172, 272.0732648951661, -43.11827466766157, 1.0, 97.38609969531454, -83.2147861711073, 146.81887040478475, 1.0, 163.08578190031804, 277.1885139051699, -33.4979780817946, 1.0])

# create a new 'Frustum Selection Source'
selection_sources29300 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.29300', FieldType='POINT',
    Frustum=[122.15460230873006, -67.23739726089983, -133.93214321119294, 1.0, -127.12916746329289, 292.78066748650417, 233.616196831503, 1.0, 122.11271761543256, -70.06056611221757, -131.6071397606959, 1.0, -127.23092867743074, 285.9216202449339, 239.26492326043396, 1.0, 129.9676435211165, -65.66429683351569, -131.88123229298859, 1.0, -108.14694514560155, 296.6026033023963, 238.59900006328633, 1.0, 129.925758827819, -68.48746568483344, -129.55622884249155, 1.0, -108.24870635973951, 289.74355606082594, 244.24772649221728, 1.0])

# create a new 'Append Selections'
selection_filter29333 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.29333', Input=selection_sources29300,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Frustum Selection Source'
selection_sources26139 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.26139', FieldType='POINT',
    Frustum=[69.20126427137032, -92.43802075529285, 44.23025421440827, 1.0, -17.007215897105414, 280.3205991227095, 63.668303530357974, 1.0, 67.4035829388476, -93.09910353939757, 48.5803899800776, 1.0, -22.423684574198283, 278.3287365337802, 76.77539525433106, 1.0, 76.52370144825859, -92.45808036098232, 47.25318229524296, 1.0, 5.055510622359405, 280.26015891902824, 72.77647802531601, 1.0, 74.72602011573588, -93.11916314508704, 51.60331806091228, 1.0, -0.36095805473340176, 278.26829633009885, 85.88356974928911, 1.0])

# create a new 'Append Selections'
selection_filter26161 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.26161', Input=selection_sources26139,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Frustum Selection Source'
selection_sources25912 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.25912', FieldType='POINT',
    Frustum=[141.1667692475011, -95.77060805672497, 89.77578856343561, 1.0, 172.2392937978527, 281.1203317721205, 9.368341527753195, 1.0, 138.60696688013664, -95.05887973797904, 95.5418584480677, 1.0, 165.87860650450656, 282.88885942530135, 23.696075541643914, 1.0, 145.69554472490543, -95.1970835696919, 91.7155112503242, 1.0, 183.4925549873883, 282.5454456651318, 14.18823293984322, 1.0, 143.135742357541, -94.48535525094597, 97.4815811349563, 1.0, 177.13186769404217, 284.31397331831266, 28.51596695373394, 1.0])

# create a new 'Frustum Selection Source'
selection_sources24766 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.24766', FieldType='POINT',
    Frustum=[126.06048736420671, -28.229783327454793, -16.941740238777, 1.0, -22.49704369942139, 193.7223035911398, 275.8081429253066, 1.0, 125.86774423481432, -41.22131690133075, -6.242642176537137, 1.0, -22.864477446644944, 168.9560362887569, 296.20425097498816, 1.0, 139.35073326871887, -25.283022619490847, -13.124171316600817, 1.0, 2.838670572788863, 199.33982849338432, 283.0857234999359, 1.0, 139.15799013932647, -38.27455619336681, -2.42507325436095, 1.0, 2.471236825565262, 174.57356119100146, 303.4818315496175, 1.0])

# create a new 'Append Selections'
selection_filter27196 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.27196', Input=selection_sources27162,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Frustum Selection Source'
selection_sources27659 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.27659', FieldType='POINT',
    Frustum=[127.62757447888038, -106.71455897943179, -98.81819053014631, 1.0, -113.83227427557631, 196.86868649955903, 318.92751647331136, 1.0, 127.54380509228534, -112.36089668206726, -94.16818362915227, 1.0, -114.03579670385204, 183.15059201641827, 330.22496933117316, 1.0, 134.8618718977567, -105.25798450963165, -96.91919893921636, 1.0, -96.25614249993612, 200.40751595871836, 323.541223169407, 1.0, 134.77810251116168, -110.90432221226713, -92.2691920382223, 1.0, -96.45966492821196, 186.68942147557772, 334.83867602726883, 1.0])

# create a new 'Append Selections'
selection_filter25946 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.25946', Input=selection_sources25912,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Append Selections'
selection_filter28024 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.28024', Input=selection_sources28001,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Frustum Selection Source'
selection_sources25879 = CreateSelection(proxyname='FrustumSelectionSource', registrationname='selection_sources.25879', FieldType='POINT',
    Frustum=[53.217652651946764, -97.48825833296152, 114.51174660803977, 1.0, -46.29977606258223, 276.8522537260333, 70.83312335192662, 1.0, 51.537782348363855, -97.02118662378449, 118.29572996982958, 1.0, -50.47397709884065, 278.01284999843324, 80.23569879854237, 1.0, 59.55793832031284, -96.6853240511152, 117.22735836968377, 1.0, -30.545210397232424, 278.847413176249, 77.5809713288526, 1.0, 57.87806801672994, -96.2182523419382, 121.01134173147358, 1.0, -34.719411433490805, 280.00800944864903, 86.98354677546837, 1.0])

# create a new 'Append Selections'
selection_filter25901 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.25901', Input=selection_sources25879,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Append Selections'
selection_filter24788 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.24788', Input=selection_sources24766,
    Expression='s0',
    SelectionNames=['s0'])

# create a new 'Append Selections'
selection_filter27694 = CreateSelection(proxyname='AppendSelections', registrationname='selection_filter.27694', Input=selection_sources27659,
    Expression='s0',
    SelectionNames=['s0'])

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
viz_calcium_in = CSVReader(registrationName='viz_calcium_in', FileName=['/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0000000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0010000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0020000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0030000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0040000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0050000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0060000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0070000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0080000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0090000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0100000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0110000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0120000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0130000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0140000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0150000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0160000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0170000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0180000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0190000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0200000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0210000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0220000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0230000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0240000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0250000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0260000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0270000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0280000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0290000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0300000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0310000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0320000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0330000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0340000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0350000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0360000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0370000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0380000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0390000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0400000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0410000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0420000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0430000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0440000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0450000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0460000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0470000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0480000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0490000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0500000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0510000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0520000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0530000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0540000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0550000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0560000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0570000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0580000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0590000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0600000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0610000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0620000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0630000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0640000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0650000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0660000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0670000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0680000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0690000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0700000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0710000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0720000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0730000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0740000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0750000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0760000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0770000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0780000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0790000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0800000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0810000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0820000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0830000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0840000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0850000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0860000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0870000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0880000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0890000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0900000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0910000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0920000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0930000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0940000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0950000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0960000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0970000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0980000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_0990000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/calcium_area/rank_0_step_1000000_in_network_areas.txt'])
viz_calcium_in.FieldDelimiterCharacters = '" "'
viz_calcium_in.AddTabFieldDelimiter = 1

# create a new 'Threshold Table'
thresholdTable_calcium_source = ThresholdTable(registrationName='ThresholdTable_calcium_source', Input=viz_calcium_in)
thresholdTable_calcium_source.Column = ['ROWS', 'SourceArea']
thresholdTable_calcium_source.MaxValue = 47.0

# create a new 'Threshold Table'
thresholdTable_calcium_target = ThresholdTable(registrationName='ThresholdTable_calcium_target', Input=viz_calcium_in)
thresholdTable_calcium_target.Column = ['ROWS', 'TargetArea']
thresholdTable_calcium_target.MaxValue = 47.0

# create a new 'Table To Points'
tableToPoints_calcium_target = TableToPoints(registrationName='TableToPoints_calcium_target', Input=thresholdTable_calcium_target)
tableToPoints_calcium_target.XColumn = 'AvgPosX'
tableToPoints_calcium_target.YColumn = 'AvgPosY'
tableToPoints_calcium_target.ZColumn = 'AvgPosZ'

# create a new 'Programmable Filter'
programmableFilter_calcium_target = ProgrammableFilter(registrationName='ProgrammableFilter_calcium_target', Input=tableToPoints_calcium_target)
programmableFilter_calcium_target.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_calcium_target.RequestInformationScript = ''
programmableFilter_calcium_target.RequestUpdateExtentScript = ''
programmableFilter_calcium_target.PythonPath = ''

# create a new 'Tube'
tube_calcium_target = Tube(registrationName='Tube_calcium_target', Input=programmableFilter_calcium_target)
tube_calcium_target.Scalars = ['POINTS', '']
tube_calcium_target.Vectors = ['POINTS', '1']
tube_calcium_target.Radius = 0.35

# create a new 'CSV Reader'
viz_stimulus_in = CSVReader(registrationName='viz_stimulus_in', FileName=['/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0000000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0010000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0020000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0030000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0040000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0050000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0060000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0070000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0080000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0090000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0100000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0110000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0120000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0130000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0140000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0150000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0160000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0170000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0180000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0190000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0200000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0210000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0220000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0230000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0240000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0250000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0260000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0270000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0280000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0290000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0300000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0310000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0320000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0330000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0340000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0350000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0360000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0370000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0380000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0390000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0400000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0410000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0420000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0430000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0440000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0450000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0460000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0470000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0480000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0490000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0500000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0510000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0520000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0530000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0540000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0550000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0560000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0570000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0580000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0590000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0600000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0610000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0620000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0630000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0640000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0650000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0660000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0670000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0680000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0690000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0700000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0710000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0720000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0730000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0740000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0750000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0760000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0770000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0780000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0790000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0800000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0810000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0820000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0830000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0840000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0850000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0860000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0870000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0880000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0890000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0900000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0910000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0920000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0930000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0940000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0950000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0960000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0970000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0980000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_0990000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/stimulus_area/rank_0_step_1000000_in_network_areas.txt'])
viz_stimulus_in.FieldDelimiterCharacters = '" "'
viz_stimulus_in.AddTabFieldDelimiter = 1

# create a new 'Threshold Table'
thresholdTable_stimulus_target = ThresholdTable(registrationName='ThresholdTable_stimulus_target', Input=viz_stimulus_in)
thresholdTable_stimulus_target.Column = ['ROWS', 'TargetArea']
thresholdTable_stimulus_target.MinValue = 32.0
thresholdTable_stimulus_target.MaxValue = 32.0

# create a new 'Table To Points'
tableToPoints_stimulus_target = TableToPoints(registrationName='TableToPoints_stimulus_target', Input=thresholdTable_stimulus_target)
tableToPoints_stimulus_target.XColumn = 'AvgPosX'
tableToPoints_stimulus_target.YColumn = 'AvgPosY'
tableToPoints_stimulus_target.ZColumn = 'AvgPosZ'

# create a new 'Programmable Filter'
programmableFilter_stimulus_target = ProgrammableFilter(registrationName='ProgrammableFilter_stimulus_target', Input=tableToPoints_stimulus_target)
programmableFilter_stimulus_target.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_stimulus_target.RequestInformationScript = ''
programmableFilter_stimulus_target.RequestUpdateExtentScript = ''
programmableFilter_stimulus_target.PythonPath = ''

# create a new 'CSV Reader'
viz_no_network_in = CSVReader(registrationName='viz_no_network_in', FileName=['/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0040000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0050000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0060000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0070000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0080000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0090000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0100000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0110000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0120000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0130000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0140000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0150000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0160000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0170000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0180000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0190000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0200000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0210000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0220000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0230000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0240000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0250000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0260000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0270000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0280000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0290000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0300000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0310000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0320000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0330000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0340000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0350000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0360000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0370000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0380000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0390000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0400000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0410000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0420000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0430000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0440000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0450000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0460000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0470000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0480000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0490000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0500000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0510000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0520000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0530000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0540000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0550000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0560000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0570000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0580000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0590000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0600000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0610000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0620000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0630000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0640000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0650000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0660000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0670000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0680000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0690000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0700000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0710000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0720000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0730000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0740000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0750000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0760000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0770000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0780000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0790000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0800000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0810000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0820000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0830000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0840000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0850000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0860000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0870000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0880000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0890000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0900000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0910000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0920000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0930000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0940000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0950000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0960000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0970000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0980000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_0990000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/no_network_area/rank_0_step_1000000_in_network_areas.txt'])
viz_no_network_in.FieldDelimiterCharacters = '" "'
viz_no_network_in.AddTabFieldDelimiter = 1

# create a new 'Threshold Table'
thresholdTable_target = ThresholdTable(registrationName='ThresholdTable_target', Input=viz_no_network_in)
thresholdTable_target.Column = ['ROWS', 'TargetArea']
thresholdTable_target.MinValue = 5.0
thresholdTable_target.MaxValue = 5.0

# create a new 'Table To Points'
tableToPoints_no_network_target = TableToPoints(registrationName='TableToPoints_no_network_target', Input=thresholdTable_target)
tableToPoints_no_network_target.XColumn = 'AvgPosX'
tableToPoints_no_network_target.YColumn = 'AvgPosY'
tableToPoints_no_network_target.ZColumn = 'AvgPosZ'

# create a new 'Programmable Filter'
programmableFilter_no_network_target = ProgrammableFilter(registrationName='ProgrammableFilter_no_network_target', Input=tableToPoints_no_network_target)
programmableFilter_no_network_target.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_no_network_target.RequestInformationScript = ''
programmableFilter_no_network_target.RequestUpdateExtentScript = ''
programmableFilter_no_network_target.PythonPath = ''

# create a new 'Tube'
tube_no_network_target = Tube(registrationName='Tube_no_network_target', Input=programmableFilter_no_network_target)
tube_no_network_target.Scalars = ['POINTS', '']
tube_no_network_target.Vectors = ['POINTS', '1']
tube_no_network_target.Radius = 0.35

# create a new 'Threshold Table'
thresholdTable_source = ThresholdTable(registrationName='ThresholdTable_source', Input=viz_no_network_in)
thresholdTable_source.Column = ['ROWS', 'SourceArea']
thresholdTable_source.MaxValue = 47.0

# create a new 'Table To Points'
tableToPoints_no_network_source = TableToPoints(registrationName='TableToPoints_no_network_source', Input=thresholdTable_source)
tableToPoints_no_network_source.XColumn = 'AvgPosX'
tableToPoints_no_network_source.YColumn = 'AvgPosY'
tableToPoints_no_network_source.ZColumn = 'AvgPosZ'

# create a new 'Extract Selection'
extractSelection_no_network_source = ExtractSelection(registrationName='ExtractSelection_no_network_source', Input=tableToPoints_no_network_source,
    Selection=selection_filter26161)

# create a new 'Annotate Attribute Data'
annotateAttributeData_no_network_source = AnnotateAttributeData(registrationName='AnnotateAttributeData_no_network_source', Input=extractSelection_no_network_source)
annotateAttributeData_no_network_source.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_no_network_source.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'Programmable Filter'
programmableFilter_no_network_source = ProgrammableFilter(registrationName='ProgrammableFilter_no_network_source', Input=tableToPoints_no_network_source)
programmableFilter_no_network_source.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_no_network_source.RequestInformationScript = ''
programmableFilter_no_network_source.RequestUpdateExtentScript = ''
programmableFilter_no_network_source.PythonPath = ''

# create a new 'Tube'
tube_no_network_source = Tube(registrationName='Tube_no_network_source', Input=programmableFilter_no_network_source)
tube_no_network_source.Scalars = ['POINTS', '']
tube_no_network_source.Vectors = ['POINTS', '1']
tube_no_network_source.Radius = 0.35

# create a new 'CSV Reader'
viz_disable_in = CSVReader(registrationName='viz_disable_in', FileName=['/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0000000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0010000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0020000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0030000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0040000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0050000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0060000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0070000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0080000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0090000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0100000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0110000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0120000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0130000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0140000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0150000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0160000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0170000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0180000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0190000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0200000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0210000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0220000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0230000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0240000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0250000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0260000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0270000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0280000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0290000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0300000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0310000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0320000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0330000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0340000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0350000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0360000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0370000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0380000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0390000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0400000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0410000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0420000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0430000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0440000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0450000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0460000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0470000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0480000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0490000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0500000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0510000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0520000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0530000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0540000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0550000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0560000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0570000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0580000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0590000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0600000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0610000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0620000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0630000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0640000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0650000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0660000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0670000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0680000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0690000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0700000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0710000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0720000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0730000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0740000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0750000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0760000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0770000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0780000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0790000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0800000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0810000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0820000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0830000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0840000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0850000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0860000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0870000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0880000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0890000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0900000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0910000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0920000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0930000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0940000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0950000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0960000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0970000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0980000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_0990000_in_network_areas.txt', '/Users/mikemeulendijks/Documents/School/SVVR/Project/disable_area/rank_0_step_1000000_in_network_areas.txt'])
viz_disable_in.FieldDelimiterCharacters = '" "'
viz_disable_in.AddTabFieldDelimiter = 1

# create a new 'Threshold Table'
thresholdTable_disable_source = ThresholdTable(registrationName='ThresholdTable_disable_source', Input=viz_disable_in)
thresholdTable_disable_source.Column = ['ROWS', 'SourceArea']
thresholdTable_disable_source.MaxValue = 47.0

# create a new 'Extract Selection'
extractSelection_stimulus_target = ExtractSelection(registrationName='ExtractSelection_stimulus_target', Input=tableToPoints_stimulus_target,
    Selection=selection_filter25946)

# create a new 'Annotate Attribute Data'
annotateAttributeData_stimulus_target = AnnotateAttributeData(registrationName='AnnotateAttributeData_stimulus_target', Input=extractSelection_stimulus_target)
annotateAttributeData_stimulus_target.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_stimulus_target.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'CSV Reader'
neurons_of_the_brain = CSVReader(registrationName='neurons_of_the_brain', FileName=['/Users/mikemeulendijks/Documents/School/SVVR/Project/rank_0_positions_edited.txt'])
neurons_of_the_brain.FieldDelimiterCharacters = '" "'
neurons_of_the_brain.AddTabFieldDelimiter = 1

# create a new 'Threshold Table'
thresholdTable_neurons_2 = ThresholdTable(registrationName='ThresholdTable_neurons_2', Input=neurons_of_the_brain)
thresholdTable_neurons_2.Column = ['ROWS', 'Area']
thresholdTable_neurons_2.MinValue = 8.0
thresholdTable_neurons_2.MaxValue = 8.0

# create a new 'Table To Points'
tableToPoints_neurons_2 = TableToPoints(registrationName='TableToPoints_neurons_2', Input=thresholdTable_neurons_2)
tableToPoints_neurons_2.XColumn = 'PosX'
tableToPoints_neurons_2.YColumn = 'PosY'
tableToPoints_neurons_2.ZColumn = 'PosZ'

# create a new 'Threshold Table'
thresholdTable_neurons_3 = ThresholdTable(registrationName='ThresholdTable_neurons_3', Input=neurons_of_the_brain)
thresholdTable_neurons_3.Column = ['ROWS', 'Area']
thresholdTable_neurons_3.MinValue = 12.0
thresholdTable_neurons_3.MaxValue = 12.0

# create a new 'Table To Points'
tableToPoints_neurons_3 = TableToPoints(registrationName='TableToPoints_neurons_3', Input=thresholdTable_neurons_3)
tableToPoints_neurons_3.XColumn = 'PosX'
tableToPoints_neurons_3.YColumn = 'PosY'
tableToPoints_neurons_3.ZColumn = 'PosZ'

# create a new 'Threshold Table'
thresholdTable_neurons = ThresholdTable(registrationName='ThresholdTable_neurons', Input=neurons_of_the_brain)
thresholdTable_neurons.Column = ['ROWS', 'Area']
thresholdTable_neurons.MaxValue = 47.0

# create a new 'Table To Points'
tableToPoints_neurons = TableToPoints(registrationName='TableToPoints_neurons', Input=thresholdTable_neurons)
tableToPoints_neurons.XColumn = 'PosX'
tableToPoints_neurons.YColumn = 'PosY'
tableToPoints_neurons.ZColumn = 'PosZ'

# create a new 'Table To Points'
tableToPoints_calcium_source = TableToPoints(registrationName='TableToPoints_calcium_source', Input=thresholdTable_calcium_source)
tableToPoints_calcium_source.XColumn = 'AvgPosX'
tableToPoints_calcium_source.YColumn = 'AvgPosY'
tableToPoints_calcium_source.ZColumn = 'AvgPosZ'

# create a new 'Programmable Filter'
programmableFilter_calcium_source = ProgrammableFilter(registrationName='ProgrammableFilter_calcium_source', Input=tableToPoints_calcium_source)
programmableFilter_calcium_source.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_calcium_source.RequestInformationScript = ''
programmableFilter_calcium_source.RequestUpdateExtentScript = ''
programmableFilter_calcium_source.PythonPath = ''

# create a new 'Tube'
tube_calcium_source = Tube(registrationName='Tube_calcium_source', Input=programmableFilter_calcium_source)
tube_calcium_source.Scalars = ['POINTS', '']
tube_calcium_source.Vectors = ['POINTS', '1']
tube_calcium_source.Radius = 0.35

# create a new 'Extract Selection'
extractSelection_calcium_target = ExtractSelection(registrationName='ExtractSelection_calcium_target', Input=tableToPoints_calcium_target,
    Selection=selection_filter28024)

# create a new 'Annotate Attribute Data'
annotateAttributeData_calcium_target = AnnotateAttributeData(registrationName='AnnotateAttributeData_calcium_target', Input=extractSelection_calcium_target)
annotateAttributeData_calcium_target.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_calcium_target.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'Threshold Table'
thresholdTable_neurons_1 = ThresholdTable(registrationName='ThresholdTable_neurons_1', Input=neurons_of_the_brain)
thresholdTable_neurons_1.Column = ['ROWS', 'Area']
thresholdTable_neurons_1.MinValue = 5.0
thresholdTable_neurons_1.MaxValue = 5.0

# create a new 'Extract Selection'
extractSelection_calcium_source = ExtractSelection(registrationName='ExtractSelection_calcium_source', Input=tableToPoints_calcium_source,
    Selection=selection_filter27694)

# create a new 'Annotate Attribute Data'
annotateAttributeData_calcium_source = AnnotateAttributeData(registrationName='AnnotateAttributeData_calcium_source', Input=extractSelection_calcium_source)
annotateAttributeData_calcium_source.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_calcium_source.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'Table To Points'
tableToPoints_neurons_1 = TableToPoints(registrationName='TableToPoints_neurons_1', Input=thresholdTable_neurons_1)
tableToPoints_neurons_1.XColumn = 'PosX'
tableToPoints_neurons_1.YColumn = 'PosY'
tableToPoints_neurons_1.ZColumn = 'PosZ'

# create a new 'Threshold Table'
thresholdTable_stimulus_source = ThresholdTable(registrationName='ThresholdTable_stimulus_source', Input=viz_stimulus_in)
thresholdTable_stimulus_source.Column = ['ROWS', 'SourceArea']
thresholdTable_stimulus_source.MaxValue = 47.0

# create a new 'Table To Points'
tableToPoints_stimulus_source = TableToPoints(registrationName='TableToPoints_stimulus_source', Input=thresholdTable_stimulus_source)
tableToPoints_stimulus_source.XColumn = 'AvgPosX'
tableToPoints_stimulus_source.YColumn = 'AvgPosY'
tableToPoints_stimulus_source.ZColumn = 'AvgPosZ'

# create a new 'Table To Points'
tableToPoints_disable_source = TableToPoints(registrationName='TableToPoints_disable_source', Input=thresholdTable_disable_source)
tableToPoints_disable_source.XColumn = 'AvgPosX'
tableToPoints_disable_source.YColumn = 'AvgPosY'
tableToPoints_disable_source.ZColumn = 'AvgPosZ'

# create a new 'Programmable Filter'
programmableFilter_disable_source = ProgrammableFilter(registrationName='ProgrammableFilter_disable_source', Input=tableToPoints_disable_source)
programmableFilter_disable_source.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_disable_source.RequestInformationScript = ''
programmableFilter_disable_source.RequestUpdateExtentScript = ''
programmableFilter_disable_source.PythonPath = ''

# create a new 'Tube'
tube_disable_source = Tube(registrationName='Tube_disable_source', Input=programmableFilter_disable_source)
tube_disable_source.Scalars = ['POINTS', '']
tube_disable_source.Vectors = ['POINTS', '1']
tube_disable_source.Radius = 0.35

# create a new 'Extract Selection'
extractSelection_disable_source = ExtractSelection(registrationName='ExtractSelection_disable_source', Input=tableToPoints_disable_source,
    Selection=selection_filter27196)

# create a new 'Annotate Attribute Data'
annotateAttributeData_disable_source = AnnotateAttributeData(registrationName='AnnotateAttributeData_disable_source', Input=extractSelection_disable_source)
annotateAttributeData_disable_source.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_disable_source.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'Threshold Table'
thresholdTable_disable_target = ThresholdTable(registrationName='ThresholdTable_disable_target', Input=viz_disable_in)
thresholdTable_disable_target.Column = ['ROWS', 'TargetArea']
thresholdTable_disable_target.MaxValue = 47.0

# create a new 'Table To Points'
tableToPoints_disable_target = TableToPoints(registrationName='TableToPoints_disable_target', Input=thresholdTable_disable_target)
tableToPoints_disable_target.XColumn = 'AvgPosX'
tableToPoints_disable_target.YColumn = 'AvgPosY'
tableToPoints_disable_target.ZColumn = 'AvgPosZ'

# create a new 'Programmable Filter'
programmableFilter_disable_target = ProgrammableFilter(registrationName='ProgrammableFilter_disable_target', Input=tableToPoints_disable_target)
programmableFilter_disable_target.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_disable_target.RequestInformationScript = ''
programmableFilter_disable_target.RequestUpdateExtentScript = ''
programmableFilter_disable_target.PythonPath = ''

# create a new 'Tube'
tube_disable_target = Tube(registrationName='Tube_disable_target', Input=programmableFilter_disable_target)
tube_disable_target.Scalars = ['POINTS', '']
tube_disable_target.Vectors = ['POINTS', '1']
tube_disable_target.Radius = 0.35

# create a new 'Extract Selection'
extractSelection_disable_target = ExtractSelection(registrationName='ExtractSelection_disable_target', Input=tableToPoints_disable_target,
    Selection=selection_filter29333)

# create a new 'Annotate Attribute Data'
annotateAttributeData_disable_target = AnnotateAttributeData(registrationName='AnnotateAttributeData_disable_target', Input=extractSelection_disable_target)
annotateAttributeData_disable_target.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_disable_target.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'Tube'
tube_stimulus_target = Tube(registrationName='Tube_stimulus_target', Input=programmableFilter_stimulus_target)
tube_stimulus_target.Scalars = ['POINTS', '']
tube_stimulus_target.Vectors = ['POINTS', '1']
tube_stimulus_target.Radius = 0.35

# create a new 'Extract Selection'
extractSelection_stimulus_source = ExtractSelection(registrationName='ExtractSelection_stimulus_source', Input=tableToPoints_stimulus_source,
    Selection=selection_filter25901)

# create a new 'Annotate Attribute Data'
annotateAttributeData_stimulus_source = AnnotateAttributeData(registrationName='AnnotateAttributeData_stimulus_source', Input=extractSelection_stimulus_source)
annotateAttributeData_stimulus_source.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_stimulus_source.Prefix = 'Note: only accurate if one area is selected. The area selected is Area : '

# create a new 'Extract Selection'
extractSelection_no_network_target = ExtractSelection(registrationName='ExtractSelection_no_network_target', Input=tableToPoints_no_network_target,
    Selection=selection_filter24788)

# create a new 'Annotate Attribute Data'
annotateAttributeData_no_network_target = AnnotateAttributeData(registrationName='AnnotateAttributeData_no_network_target', Input=extractSelection_no_network_target)
annotateAttributeData_no_network_target.SelectInputArray = ['POINTS', 'Area']
annotateAttributeData_no_network_target.Prefix = 'Note: only accurate if one area is selected. The area selected is Area '

# create a new 'Programmable Filter'
programmableFilter_stimulus_source = ProgrammableFilter(registrationName='ProgrammableFilter_stimulus_source', Input=tableToPoints_stimulus_source)
programmableFilter_stimulus_source.Script = """import vtk

def lines_from_points(pd, weights):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    # Add weight data as a scalar attribute
    weight_data = vtk.vtkFloatArray()
    weight_data.SetName("Weights")

    for i in range(pd.GetNumberOfPoints() // 2):
        # Get the weight for the line
        weight = weights.GetTuple1(i)  # Assuming each line corresponds to a point pair
        weight_data.InsertNextValue(weight)

        # gets source and target points
        source = pd.GetPoint(2 * i)
        target = pd.GetPoint(2 * i + 1)

        # adds points
        source_id = points.InsertNextPoint(source)
        target_id = points.InsertNextPoint(target)

        # creates a line
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, source_id)
        line.GetPointIds().SetId(1, target_id)
        lines.InsertNextCell(line)

    # creates a polydata object to store the lines
    lines_pd = vtk.vtkPolyData()
    lines_pd.SetPoints(points)
    lines_pd.SetLines(lines)
    lines_pd.GetCellData().SetScalars(weight_data)

    return lines_pd

input_data = inputs[0]
weights = input_data.GetPointData().GetArray("SumWeights")  # Extract weights

# extracts coordinates and creates points
new_points = vtk.vtkPoints()
for i in range(input_data.GetNumberOfPoints()):
    point = input_data.GetPoint(i)
    new_points.InsertNextPoint(point[:3])

# Generate lines with weights
output.ShallowCopy(lines_from_points(new_points, weights))"""
programmableFilter_stimulus_source.RequestInformationScript = ''
programmableFilter_stimulus_source.RequestUpdateExtentScript = ''
programmableFilter_stimulus_source.PythonPath = ''

# create a new 'Tube'
tube_stimulus_source = Tube(registrationName='Tube_stimulus_source', Input=programmableFilter_stimulus_source)
tube_stimulus_source.Scalars = ['POINTS', '']
tube_stimulus_source.Vectors = ['POINTS', '1']
tube_stimulus_source.Radius = 0.35

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tableToPoints_neurons
tableToPoints_neuronsDisplay = Show(tableToPoints_neurons, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'Area'
areaTF2D = GetTransferFunction2D('Area')

# get color transfer function/color map for 'Area'
areaLUT = GetColorTransferFunction('Area')
areaLUT.InterpretValuesAsCategories = 1
areaLUT.AnnotationsInitialized = 1
areaLUT.TransferFunction2D = areaTF2D
areaLUT.RGBPoints = [0.0, 0.267004, 0.004874, 0.329415, 0.184334, 0.26851, 0.009605, 0.335427, 0.368621, 0.269944, 0.014625, 0.341379, 0.552955, 0.271305, 0.019942, 0.347269, 0.737242, 0.272594, 0.025563, 0.353093, 0.9215760000000001, 0.273809, 0.031497, 0.358853, 1.105863, 0.274952, 0.037752, 0.364543, 1.290197, 0.276022, 0.044167, 0.370164, 1.4745309999999998, 0.277018, 0.050344, 0.375715, 1.658818, 0.277941, 0.056324, 0.381191, 1.8431520000000001, 0.278791, 0.062145, 0.386592, 2.027439, 0.279566, 0.067836, 0.391917, 2.211773, 0.280267, 0.073417, 0.397163, 2.39606, 0.280894, 0.078907, 0.402329, 2.580394, 0.281446, 0.08432, 0.407414, 2.764728, 0.281924, 0.089666, 0.412415, 2.9490149999999997, 0.282327, 0.094955, 0.417331, 3.1333490000000004, 0.282656, 0.100196, 0.42216, 3.317636, 0.28291, 0.105393, 0.426902, 3.5019700000000005, 0.283091, 0.110553, 0.431554, 3.686257, 0.283197, 0.11568, 0.436115, 3.8705909999999997, 0.283229, 0.120777, 0.440584, 4.054925, 0.283187, 0.125848, 0.44496, 4.239212, 0.283072, 0.130895, 0.449241, 4.423546, 0.282884, 0.13592, 0.453427, 4.607833, 0.282623, 0.140926, 0.457517, 4.792167, 0.28229, 0.145912, 0.46151, 4.976454, 0.281887, 0.150881, 0.465405, 5.160788, 0.281412, 0.155834, 0.469201, 5.3450750000000005, 0.280868, 0.160771, 0.472899, 5.529409, 0.280255, 0.165693, 0.476498, 5.713743, 0.279574, 0.170599, 0.479997, 5.898029999999999, 0.278826, 0.17549, 0.483397, 6.082364, 0.278012, 0.180367, 0.486697, 6.266651, 0.277134, 0.185228, 0.489898, 6.450984999999999, 0.276194, 0.190074, 0.493001, 6.635272, 0.275191, 0.194905, 0.496005, 6.819606, 0.274128, 0.199721, 0.498911, 7.003940000000001, 0.273006, 0.20452, 0.501721, 7.1882269999999995, 0.271828, 0.209303, 0.504434, 7.372561, 0.270595, 0.214069, 0.507052, 7.5568480000000005, 0.269308, 0.218818, 0.509577, 7.741181999999999, 0.267968, 0.223549, 0.512008, 7.925469, 0.26658, 0.228262, 0.514349, 8.109803000000001, 0.265145, 0.232956, 0.516599, 8.294137, 0.263663, 0.237631, 0.518762, 8.478424, 0.262138, 0.242286, 0.520837, 8.662758, 0.260571, 0.246922, 0.522828, 8.847045000000001, 0.258965, 0.251537, 0.524736, 9.031379, 0.257322, 0.25613, 0.526563, 9.215666, 0.255645, 0.260703, 0.528312, 9.4, 0.253935, 0.265254, 0.529983, 9.584334, 0.252194, 0.269783, 0.531579, 9.768621, 0.250425, 0.27429, 0.533103, 9.952955000000001, 0.248629, 0.278775, 0.534556, 10.137241999999999, 0.246811, 0.283237, 0.535941, 10.321576, 0.244972, 0.287675, 0.53726, 10.505863, 0.243113, 0.292092, 0.538516, 10.690197, 0.241237, 0.296485, 0.539709, 10.874531, 0.239346, 0.300855, 0.540844, 11.058818, 0.237441, 0.305202, 0.541921, 11.243152, 0.235526, 0.309527, 0.542944, 11.427439, 0.233603, 0.313828, 0.543914, 11.611773, 0.231674, 0.318106, 0.544834, 11.796059999999999, 0.229739, 0.322361, 0.545706, 11.980394, 0.227802, 0.326594, 0.546532, 12.164728, 0.225863, 0.330805, 0.547314, 12.349015, 0.223925, 0.334994, 0.548053, 12.533349, 0.221989, 0.339161, 0.548752, 12.717636, 0.220057, 0.343307, 0.549413, 12.901969999999999, 0.21813, 0.347432, 0.550038, 13.086257, 0.21621, 0.351535, 0.550627, 13.270591000000001, 0.214298, 0.355619, 0.551184, 13.454925, 0.212395, 0.359683, 0.55171, 13.639212, 0.210503, 0.363727, 0.552206, 13.823546, 0.208623, 0.367752, 0.552675, 14.007833, 0.206756, 0.371758, 0.553117, 14.192167, 0.204903, 0.375746, 0.553533, 14.376453999999999, 0.203063, 0.379716, 0.553925, 14.560788, 0.201239, 0.38367, 0.554294, 14.745074999999998, 0.19943, 0.387607, 0.554642, 14.929409, 0.197636, 0.391528, 0.554969, 15.113743, 0.19586, 0.395433, 0.555276, 15.29803, 0.1941, 0.399323, 0.555565, 15.482363999999999, 0.192357, 0.403199, 0.555836, 15.666651, 0.190631, 0.407061, 0.556089, 15.850985000000001, 0.188923, 0.41091, 0.556326, 16.035272, 0.187231, 0.414746, 0.556547, 16.219606000000002, 0.185556, 0.41857, 0.556753, 16.40394, 0.183898, 0.422383, 0.556944, 16.588227, 0.182256, 0.426184, 0.55712, 16.772561, 0.180629, 0.429975, 0.557282, 16.956848, 0.179019, 0.433756, 0.55743, 17.141182, 0.177423, 0.437527, 0.557565, 17.325469, 0.175841, 0.44129, 0.557685, 17.509803, 0.174274, 0.445044, 0.557792, 17.694137, 0.172719, 0.448791, 0.557885, 17.878424, 0.171176, 0.45253, 0.557965, 18.062758, 0.169646, 0.456262, 0.55803, 18.247045, 0.168126, 0.459988, 0.558082, 18.431379, 0.166617, 0.463708, 0.558119, 18.615666, 0.165117, 0.467423, 0.558141, 18.8, 0.163625, 0.471133, 0.558148, 18.984334, 0.162142, 0.474838, 0.55814, 19.168621, 0.160665, 0.47854, 0.558115, 19.352954999999998, 0.159194, 0.482237, 0.558073, 19.537242, 0.157729, 0.485932, 0.558013, 19.721576, 0.15627, 0.489624, 0.557936, 19.905863, 0.154815, 0.493313, 0.55784, 20.090197, 0.153364, 0.497, 0.557724, 20.274531, 0.151918, 0.500685, 0.557587, 20.458818, 0.150476, 0.504369, 0.55743, 20.643152, 0.149039, 0.508051, 0.55725, 20.827439000000002, 0.147607, 0.511733, 0.557049, 21.011772999999998, 0.14618, 0.515413, 0.556823, 21.19606, 0.144759, 0.519093, 0.556572, 21.380394, 0.143343, 0.522773, 0.556295, 21.564728, 0.141935, 0.526453, 0.555991, 21.749015, 0.140536, 0.530132, 0.555659, 21.933349, 0.139147, 0.533812, 0.555298, 22.117636, 0.13777, 0.537492, 0.554906, 22.30197, 0.136408, 0.541173, 0.554483, 22.486257, 0.135066, 0.544853, 0.554029, 22.670590999999998, 0.133743, 0.548535, 0.553541, 22.854925, 0.132444, 0.552216, 0.553018, 23.039212000000003, 0.131172, 0.555899, 0.552459, 23.223546, 0.129933, 0.559582, 0.551864, 23.407833, 0.128729, 0.563265, 0.551229, 23.592167, 0.127568, 0.566949, 0.550556, 23.776454, 0.126453, 0.570633, 0.549841, 23.960788, 0.125394, 0.574318, 0.549086, 24.145075, 0.124395, 0.578002, 0.548287, 24.329409, 0.123463, 0.581687, 0.547445, 24.513742999999998, 0.122606, 0.585371, 0.546557, 24.69803, 0.121831, 0.589055, 0.545623, 24.882364, 0.121148, 0.592739, 0.544641, 25.066650999999997, 0.120565, 0.596422, 0.543611, 25.250985, 0.120092, 0.600104, 0.54253, 25.435272, 0.119738, 0.603785, 0.5414, 25.619605999999997, 0.119512, 0.607464, 0.540218, 25.803939999999997, 0.119423, 0.611141, 0.538982, 25.988227000000002, 0.119483, 0.614817, 0.537692, 26.172560999999998, 0.119699, 0.61849, 0.536347, 26.356848, 0.120081, 0.622161, 0.534946, 26.541182000000003, 0.120638, 0.625828, 0.533488, 26.725469, 0.12138, 0.629492, 0.531973, 26.909803, 0.122312, 0.633153, 0.530398, 27.094136999999996, 0.123444, 0.636809, 0.528763, 27.278424, 0.12478, 0.640461, 0.527068, 27.462758, 0.126326, 0.644107, 0.525311, 27.647045, 0.128087, 0.647749, 0.523491, 27.831379000000002, 0.130067, 0.651384, 0.521608, 28.015666, 0.132268, 0.655014, 0.519661, 28.2, 0.134692, 0.658636, 0.517649, 28.384334, 0.137339, 0.662252, 0.515571, 28.568621, 0.14021, 0.665859, 0.513427, 28.752955, 0.143303, 0.669459, 0.511215, 28.937241999999998, 0.146616, 0.67305, 0.508936, 29.121576, 0.150148, 0.676631, 0.506589, 29.305863, 0.153894, 0.680203, 0.504172, 29.490197, 0.157851, 0.683765, 0.501686, 29.674530999999998, 0.162016, 0.687316, 0.499129, 29.858818, 0.166383, 0.690856, 0.496502, 30.043152, 0.170948, 0.694384, 0.493803, 30.227438999999997, 0.175707, 0.6979, 0.491033, 30.411773000000004, 0.180653, 0.701402, 0.488189, 30.59606, 0.185783, 0.704891, 0.485273, 30.780393999999998, 0.19109, 0.708366, 0.482284, 30.964727999999997, 0.196571, 0.711827, 0.479221, 31.149015000000002, 0.202219, 0.715272, 0.476084, 31.333349000000002, 0.20803, 0.718701, 0.472873, 31.517636, 0.214, 0.722114, 0.469588, 31.701970000000003, 0.220124, 0.725509, 0.466226, 31.886257, 0.226397, 0.728888, 0.462789, 32.070591, 0.232815, 0.732247, 0.459277, 32.254925, 0.239374, 0.735588, 0.455688, 32.439212000000005, 0.24607, 0.73891, 0.452024, 32.623546, 0.252899, 0.742211, 0.448284, 32.807832999999995, 0.259857, 0.745492, 0.444467, 32.992166999999995, 0.266941, 0.748751, 0.440573, 33.176454, 0.274149, 0.751988, 0.436601, 33.360788, 0.281477, 0.755203, 0.432552, 33.545075000000004, 0.288921, 0.758394, 0.428426, 33.729409000000004, 0.296479, 0.761561, 0.424223, 33.913743000000004, 0.304148, 0.764704, 0.419943, 34.09803, 0.311925, 0.767822, 0.415586, 34.282364, 0.319809, 0.770914, 0.411152, 34.466651, 0.327796, 0.77398, 0.40664, 34.650985, 0.335885, 0.777018, 0.402049, 34.835271999999996, 0.344074, 0.780029, 0.397381, 35.019606, 0.35236, 0.783011, 0.392636, 35.20394, 0.360741, 0.785964, 0.387814, 35.388227, 0.369214, 0.788888, 0.382914, 35.572561, 0.377779, 0.791781, 0.377939, 35.756848, 0.386433, 0.794644, 0.372886, 35.941182, 0.395174, 0.797475, 0.367757, 36.125468999999995, 0.404001, 0.800275, 0.362552, 36.309803, 0.412913, 0.803041, 0.357269, 36.494137, 0.421908, 0.805774, 0.35191, 36.678424, 0.430983, 0.808473, 0.346476, 36.862758, 0.440137, 0.811138, 0.340967, 37.047045000000004, 0.449368, 0.813768, 0.335384, 37.231379, 0.458674, 0.816363, 0.329727, 37.415665999999995, 0.468053, 0.818921, 0.323998, 37.6, 0.477504, 0.821444, 0.318195, 37.784334, 0.487026, 0.823929, 0.312321, 37.968621, 0.496615, 0.826376, 0.306377, 38.152955, 0.506271, 0.828786, 0.300362, 38.337242, 0.515992, 0.831158, 0.294279, 38.521576, 0.525776, 0.833491, 0.288127, 38.705863, 0.535621, 0.835785, 0.281908, 38.890197, 0.545524, 0.838039, 0.275626, 39.074531, 0.555484, 0.840254, 0.269281, 39.258818, 0.565498, 0.84243, 0.262877, 39.443152, 0.575563, 0.844566, 0.256415, 39.627439, 0.585678, 0.846661, 0.249897, 39.811773, 0.595839, 0.848717, 0.243329, 39.99606, 0.606045, 0.850733, 0.236712, 40.180394, 0.616293, 0.852709, 0.230052, 40.364728, 0.626579, 0.854645, 0.223353, 40.549015, 0.636902, 0.856542, 0.21662, 40.733349, 0.647257, 0.8584, 0.209861, 40.917636, 0.657642, 0.860219, 0.203082, 41.10197, 0.668054, 0.861999, 0.196293, 41.286257, 0.678489, 0.863742, 0.189503, 41.470591000000006, 0.688944, 0.865448, 0.182725, 41.654925, 0.699415, 0.867117, 0.175971, 41.839211999999996, 0.709898, 0.868751, 0.169257, 42.023545999999996, 0.720391, 0.87035, 0.162603, 42.207833, 0.730889, 0.871916, 0.156029, 42.392167, 0.741388, 0.873449, 0.149561, 42.576454, 0.751884, 0.874951, 0.143228, 42.760788, 0.762373, 0.876424, 0.137064, 42.945075, 0.772852, 0.877868, 0.131109, 43.129409, 0.783315, 0.879285, 0.125405, 43.313742999999995, 0.79376, 0.880678, 0.120005, 43.49803, 0.804182, 0.882046, 0.114965, 43.682364, 0.814576, 0.883393, 0.110347, 43.866651, 0.82494, 0.88472, 0.106217, 44.050985, 0.83527, 0.886029, 0.102646, 44.235272, 0.845561, 0.887322, 0.099702, 44.419606, 0.85581, 0.888601, 0.097452, 44.60394, 0.866013, 0.889868, 0.095953, 44.788227, 0.876168, 0.891125, 0.09525, 44.972561, 0.886271, 0.892374, 0.095374, 45.156848, 0.89632, 0.893616, 0.096335, 45.341181999999996, 0.906311, 0.894855, 0.098125, 45.525469, 0.916242, 0.896091, 0.100717, 45.709803, 0.926106, 0.89733, 0.104071, 45.894137, 0.935904, 0.89857, 0.108131, 46.078424000000005, 0.945636, 0.899815, 0.112838, 46.262758, 0.9553, 0.901065, 0.118128, 46.447044999999996, 0.964894, 0.902323, 0.123941, 46.631378999999995, 0.974417, 0.90359, 0.130215, 46.815666, 0.983868, 0.904867, 0.136897, 47.0, 0.993248, 0.906157, 0.143936]
areaLUT.NanColor = [1.0, 0.0, 0.0]
areaLUT.ScalarRangeInitialized = 1.0
areaLUT.Annotations = ['1', '1', '0', '0', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11', '12', '12', '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18', '18', '19', '19', '20', '20', '21', '21', '22', '22', '23', '23', '24', '24', '25', '25', '26', '26', '27', '27', '28', '28', '29', '29', '30', '30', '31', '31', '32', '32', '33', '33', '34', '34', '35', '35', '36', '36', '37', '37', '38', '38', '39', '39', '40', '40', '41', '41', '42', '42', '43', '43', '44', '44', '45', '45', '46', '46', '47', '47', '', '']
areaLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '3', '7', '10', '11', '15', '17', '19', '20', '31', '37', '40', '3', '7', '10', '11', '15', '17', '18', '19', '20', '31', '37', '40', '16', '22', '27', '28', '36', '38', '41', '42', '44', '21', '23', '24', '25', '30', '43', '45', '46', '10', '13', '26', '2', '29', '36', '16', '13', '21', '34', '39', '14', '12', '32', '35', '27', '33', '11', '47', '42']
areaLUT.IndexedColors = [0.0, 0.0, 0.0, 0.7019607843137254, 1.0, 0.7529411764705882, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5000076295109483, 0.7499961852445258, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483, 1.0, 1.0, 1.0, 0.7176470588235294, 0.0, 0.0, 0.0, 0.6901960784313725, 0.0, 0.0, 0.0, 0.5725490196078431, 0.7058823529411765, 0.7058823529411765, 0.0, 0.7372549019607844, 0.0, 0.7372549019607844, 0.0, 0.7058823529411765, 0.7058823529411765, 0.44313725490196076, 0.44313725490196076, 0.7019607843137254, 0.9882352941176471, 0.7372549019607844, 0.48627450980392156, 0.5294117647058824, 0.26666666666666666, 0.396078431372549, 0.6352941176470588, 0.4235294117647059, 0.8470588235294118, 0.43529411764705883, 0.3215686274509804, 0.2196078431372549, 0.6980392156862745, 0.6980392156862745, 0.6980392156862745, 0.6666666666666666, 0.0, 0.4980392156862745, 0.0, 0.35294117647058826, 0.0, 0.1843137254901961, 0.5450980392156862, 0.8196078431372549, 1.0, 0.6274509803921569, 0.16862745098039217, 1.0, 0.11372549019607843, 0.7647058823529411, 0.2901960784313726, 1.0, 0.8, 1.0, 0.788235294117647, 0.8196078431372549, 0.6705882352941176, 0.6509803921568628, 0.5803921568627451, 1.0, 0.788235294117647, 0.9529411764705882, 0.7019607843137254, 0.047058823529411764, 0.5058823529411764, 1.0, 0.9019607843137255, 0.6, 0.7568627450980392, 1.0, 0.19215686274509805, 0.14901960784313725, 0.6313725490196078, 1.0, 0.8313725490196079, 1.0, 0.984313725490196, 0.7686274509803922, 0.6352941176470588, 0.6352941176470588, 0.8705882352941177, 0.8862745098039215, 0.5882352941176471, 0.2980392156862745, 0.0, 0.2980392156862745, 0.38823529411764707, 0.7843137254901961, 1.0, 0.3137254901960784, 0.47843137254901963, 0.5254901960784314, 0.9372549019607843, 0.7098039215686275, 1.0, 0.8941176470588236, 0.43137254901960786, 0.3411764705882353, 0.7019607843137254, 0.00392156862745098, 0.4235294117647059, 1.0, 0.7499961852445258, 0.5000076295109483]
areaLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
areaLUT.EnableOpacityMapping = 1

# trace defaults for the display properties.
tableToPoints_neuronsDisplay.Representation = 'Points'
tableToPoints_neuronsDisplay.ColorArrayName = ['POINTS', 'Area']
tableToPoints_neuronsDisplay.LookupTable = areaLUT
tableToPoints_neuronsDisplay.Opacity = 0.4
tableToPoints_neuronsDisplay.PointSize = 3.0
tableToPoints_neuronsDisplay.RenderPointsAsSpheres = 1
tableToPoints_neuronsDisplay.Specular = 1.0
tableToPoints_neuronsDisplay.SelectTCoordArray = 'None'
tableToPoints_neuronsDisplay.SelectNormalArray = 'None'
tableToPoints_neuronsDisplay.SelectTangentArray = 'None'
tableToPoints_neuronsDisplay.OSPRayScaleArray = 'Area'
tableToPoints_neuronsDisplay.OSPRayScaleFunction = 'Piecewise Function'
tableToPoints_neuronsDisplay.Assembly = ''
tableToPoints_neuronsDisplay.SelectOrientationVectors = 'None'
tableToPoints_neuronsDisplay.ScaleFactor = 14.972908000000002
tableToPoints_neuronsDisplay.SelectScaleArray = 'Area'
tableToPoints_neuronsDisplay.GlyphType = 'Arrow'
tableToPoints_neuronsDisplay.GlyphTableIndexArray = 'Area'
tableToPoints_neuronsDisplay.GaussianRadius = 0.7486454
tableToPoints_neuronsDisplay.SetScaleArray = ['POINTS', 'Area']
tableToPoints_neuronsDisplay.ScaleTransferFunction = 'Piecewise Function'
tableToPoints_neuronsDisplay.OpacityArray = ['POINTS', 'Area']
tableToPoints_neuronsDisplay.OpacityTransferFunction = 'Piecewise Function'
tableToPoints_neuronsDisplay.DataAxesGrid = 'Grid Axes Representation'
tableToPoints_neuronsDisplay.PolarAxes = 'Polar Axes Representation'
tableToPoints_neuronsDisplay.SelectInputVectors = [None, '']
tableToPoints_neuronsDisplay.WriteLog = ''

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Area'
areaPWF = GetOpacityTransferFunction('Area')
areaPWF.Points = [0.0, 0.0, 0.5, 0.0, 47.0, 1.0, 0.5, 0.0]
areaPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper
timeKeeper1.SuppressedTimeSources = [tableToPoints_disable_source, tableToPoints_disable_target]

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0
animationScene1.EndTime = 100.0
animationScene1.PlayMode = 'Snap To TimeSteps'

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(neurons_of_the_brain)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------