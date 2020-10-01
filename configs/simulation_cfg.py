import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import os 

relBase = os.environ['CMSSW_BASE']

process = cms.Process("AOD2NanoAOD")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "WARNING"
process.MessageLogger.categories.append("AOD2NanoAOD")
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit=cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True))

# Set the maximum number of events to be processed (-1 processes all events)
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

##### ------ This set of file setup is for LOTS of files, not a short test ------
# Define files of dataset
#files = FileUtils.loadListFromFile("data/CMS_MonteCarlo2012_Summer12_DR53X_TTbar_8TeV-Madspin_aMCatNLO-herwig_AODSIM_PU_S10_START53_V19-v2_00000_file_index.txt")
#files.extend(FileUtils.loadListFromFile("data/CMS_MonteCarlo2012_Summer12_DR53X_TTbar_8TeV-Madspin_aMCatNLO-herwig_AODSIM_PU_S10_START53_V19-v2_20000_file_index.txt"))

#process.source = cms.Source(
#   "PoolSource", fileNames=cms.untracked.vstring(*files))

##### ------- This is a test file
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring('root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/TTbar_8TeV-Madspin_aMCatNLO-herwig/AODSIM/PU_S10_START53_V19-v2/00000/000A9D3F-CE4C-E311-84F8-001E673969D2.root'))
#        fileNames = cms.untracked.vstring('root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/AODSIM/PU_RD1_START53_V7N-v1/00000/000EFD4D-E1D0-E311-885A-0017A4770430.root'))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(20))

# Set global tag
# We don't have set the global tag for the educational samples. This simplifies running the code since we don't have to access the database.
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = "START53_V27::All"

# Number of events to be skipped (0 by default)
process.source.skipEvents = cms.untracked.uint32(0)

# Register fileservice for output file
process.aod2nanoaod = cms.EDAnalyzer("AOD2NanoAOD", 
        jecL1Name = cms.FileInPath('workspace/AOD2NanoAODOutreachTool/JEC_MC/START53_V27_L1FastJet_AK5PF.txt'),
        jecL2Name = cms.FileInPath('workspace/AOD2NanoAODOutreachTool/JEC_MC/START53_V27_L2Relative_AK5PF.txt'),
        jecL3Name = cms.FileInPath('workspace/AOD2NanoAODOutreachTool/JEC_MC/START53_V27_L3Absolute_AK5PF.txt'),
        jecUncName = cms.FileInPath('workspace/AOD2NanoAODOutreachTool/JEC_MC/START53_V27_Uncertainty_AK5PF.txt'),
        isData = cms.bool(False)
        )

process.TFileService = cms.Service(
    "TFileService", fileName=cms.string("output.root"))

process.p = cms.Path(process.aod2nanoaod)

