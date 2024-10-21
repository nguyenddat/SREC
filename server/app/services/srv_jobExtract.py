from srv_cvExtract import CvExtract
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

class JobExtract(CvExtract):
    """
    Class sử dụng cho Job extract
    Attributes:
        __client: OPENAI client instance
        __embeddings: Embedding model 
        schema, schema_parser: Cached schema instance
        prompt_template: Cached prompt template
    """
    def __init__(self):
        super().__init__()

    def init_schema(self):
        name_field = ResponseSchema(name="name", description=f"Based on the job's description document, extract the job's name. Please return the answer as a string.")
        age_field = ResponseSchema(name="age", description="Based on the job's description document and extract job's age requirement. Please return the answer as a string. Use 'none' if it is not available")
        experience_field = ResponseSchema(name="experience", description="Based on the experience requirement segment of the job's description document, extract all the job's working experience required. The working experience information will have two sub-infors: number of years has been working and working roles. Please return the answer as a string.")
        skills_field = ResponseSchema(name="skills", description="Based on the skills requirement segment of the job's description document (also remind to check the experience information for full skills requirements), extract all names of skills that job requires candidate to certainly have for the need of the job. Skills include both soft skills such as analytical thinking, logical thinking, problems solving, communication, etc and technical skills such as python, backend, fronend, css, c++, etc. Please return the answer as a string.")
        academic_field = ResponseSchema(name="academic", description="Based on the job's description document, extract type of academic qualification that job requires candidate to have.")
        major_field = ResponseSchema(name="major", description="Based on the academic information, extract job's major requirement. Please return the answer as a string.")
        language_field = ResponseSchema(name="language", description="Based on the job's description document, extract all languages that job requires candidate to be able to use. Please return the answer as a string.")
        certificate_field = ResponseSchema(name="certificate", description="Based on the job's description document, extract all names of certificates that job requires candidate to certainly have for the need of the job. Please return the answer as a string.")
        personality_field = ResponseSchema(name="personality", description="Based on the job's description document, extract all the job's preferred personality traits. Use 'none' if it is not available. Please return the answer as a string.")

        preferred_skills_field = ResponseSchema(name="preferred_skills", description="Based on the job's description document, extract all the job's skills that highly valued but not required. Use 'none' if it is not available. Preferred skills can be writen in the 'highly valued but not required' segment or in the skills information of the job description document. Please return the answer as a string.")
        preferred_certificate_field = ResponseSchema(name="preferred_certificate", description="Based on the job's description document, extract all certificates that highly valued but not required. Use 'none' if it is not available. Preferred certificates can be writen in the 'highly valued but not required' segment or in the skills information of the job description document. Please return the answer as a string.")

        conversation_metadata_output_schema_parser = StructuredOutputParser.from_response_schemas(
            [
                name_field,
                age_field,
                skills_field,
                academic_field,
                major_field,
                language_field,
                certificate_field,
                experience_field,
                personality_field,
                preferred_skills_field,
                preferred_certificate_field
            ]
        )
        conversation_metadata_output_schema = conversation_metadata_output_schema_parser.get_format_instructions()
        return conversation_metadata_output_schema, conversation_metadata_output_schema_parser

    def extract_category(self, file_dir):
        conversation_metadata_detected = self.extract(file_dir)
        categories = []
        job_for_return = {}
        job_string = []
        job_skills = job_certificates = []
        for category, segment in conversation_metadata_detected.items():
            if segment in ("none", ""):
                continue
            if category in ("skills", "perferred_skills"):
                job_skills.append(segment)
                continue
            elif category in ("certificate", "perferred_certificate"):
                job_certificates.append(segment)
                continue
            job_for_return.update({category: segment})
            if category not in ("name", "age"):
                categories.append(category)
                job_string.append(f"{category}: {segment}")
        if len(job_skills) != 0:
            job_skills = ", ".join(job_skills)
            categories.append("skills")
            job_for_return.update({"skills": job_skills})
            job_string.append(f"skills: {job_skills}")
        if len(job_certificates) != 0:
            job_certificates = ", ".join(job_certificates)
            categories.append("certificates")
            job_for_return.update({"certificates": job_certificates})
            job_string.append(f"certificate: {job_certificates}")
        
        job_string = "; ".join(job_string.sort(lambda x: x[0]))
        return job_for_return, job_string, categories