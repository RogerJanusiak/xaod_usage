
rucio_zee_r21_mc = 'rucio://mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00'

# Define the local dataset (per-machine), and datatype that uses it
from func_adl_servicex_xaodr21.event_collection import Event
from func_adl_servicex import SXLocalxAOD
from pathlib import Path

class xAODLocalTyped(SXLocalxAOD[Event]):
    def __init__(self, file_path: Path):
        super().__init__(file_path, item_type=Event)

local_xaod_path = Path(r"C:\Users\gordo\Code\atlas\data\xAODSampleFiles\DAOD_EXOT15.26710781._000001.pool.root.1")