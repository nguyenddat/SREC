import logging
from typing import Any
from app.services import srv_cvExtract, srv_cvMatching, srv_jobExtract

cvExtract = srv_cvExtract.CvExtract()
jobExtract = srv_jobExtract.JobExtract()
cvMatching = srv_cvMatching.CvMatching()

router = APIRouter()
logger = logging.getLogger()


