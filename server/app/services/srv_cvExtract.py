import os
import docx
import openai
from dotenv import load_dotenv
from typing import Tuple
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()
class CvExtract(object):
    """
    Class sử dụng cho CV extract và matching

    Attributes:
        __client: OPENAI client instance
        schema, schema_parser: Cached schema instance
        prompt_template: Cached prompt template
    """
    def __init__(self):
        self.__client = openai.OpenAI()
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.schema, self.schema_parser = self.init_schema()

        self.prompt_template = self.init_prompt_template()
    @property
    def supported_formats(self) -> Tuple[str]:
        return (".pdf", ".docx")

    def init_schema(self):
        name_field = ResponseSchema(name="name", description="Based on the candidate's resume document, extract the candidate's name. In a resume, there must be the candidate's name information somewhere in the candidate's resume document (oftens on header, top of the document or in the personal information segment). Please return the answer as a string")
        age_field = ResponseSchema(name="age", description="Based on the candidate's resume document and extract the candidate's age. Please return the answer as a string. Use 'none' if it is not available")
        gmail_field = ResponseSchema(name="gmail", description="Based on the candidate's resume document and extract the candidate's gmail. Gmail often ends with @gmail.com or @email.com. Please return the answer as a string")
        skills_field = ResponseSchema(name="skills", description="Based on the skills segment and project segment of the candidate's resume document, extract names of skills that candidate has. Please return the answer as a string.")
        academic_field = ResponseSchema(name="academic", description="Based on the candidate's resume document, extract type of academic qualification that candidate has. Please return the answer as a string.")
        major_field = ResponseSchema(name="major", description="Based on the academic information, extract the candidate's major field. Please return the answer as a string.")
        language_field = ResponseSchema(name="language", description="Based on the candidate's resume document, extract languages that candidate can use. Please return the answer as a string.")
        certificate_field = ResponseSchema(name="certificate", description="Based on the candidate's resume document, extract names of certificates that candidate has. Please return the answer as a string.")
        experience_field = ResponseSchema(name="experience", description="Based on the experience segment and project segment of the candidate's resume document, extract the candidate's working experience information. The working experience information will have two sub-infors: number of years has been working and working roles. Please return the answer as a string")
        personality_field = ResponseSchema(name="personality", description="Based on the candidate's resume document, extract the candidates's personality traits. User 'none' if it is not available. Please return the answer as a string.")

        conversation_metadata_output_schema_parser = StructuredOutputParser.from_response_schemas(
            [
                name_field,
                age_field,
                gmail_field,
                skills_field,
                academic_field,
                major_field,
                language_field,
                certificate_field,
                experience_field,
                personality_field
            ]
        )

        conversation_metadata_output_schema = conversation_metadata_output_schema_parser.get_format_instructions()
        return conversation_metadata_output_schema, conversation_metadata_output_schema_parser

    def init_prompt_template(self):        
        conversation_metadata_prompt_template_str = """
        Given in input text document of a candidate's resume,\
        extract the following metadata according to the format instructions below.
        
        << FORMATTING >>
        {format_instructions}
        
        << INPUT >>
        {chat_history}
        
        << OUTPUT (remember to include the ```json)>>"""
        conversation_metadata_prompt_template = PromptTemplate.from_template(template=conversation_metadata_prompt_template_str)
        return conversation_metadata_prompt_template

    def convert_file_to_text(self, file_dir):
        text: str = None
        try:
            if file_dir.endswith(".pdf"):
                loader = PyPDFLoader(file_dir)
                pages = loader.load.load_and_split()
                raw_text = [page.page_content for page in pages]
                return "\n".join([_.lower().strip() for _ in raw_text.split("\n")])
            elif file_dir.endswith(".docx"):
                doc = docx.Documnet(file_dir)
                text = "\n".join([para.text.lower().strip() for para in doc.paragraphs])
            return text
        except:
            return ""
    
    def get_completion(self, prompt):
        messages = [{"role": "user","content": prompt}]
        response = self.__client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message.content  

    def extract(self, file_dir):
        text = self.convert_file_to_text(file_dir)
        message = [{"role": "user", "content": text}]
        
        conversation_metadata_detected_str = self.get_completion((
            self.prompt.format(
                chat_history = message,
                format_instructions = self.schema
            )
        ))
        
        conversation_metadata_detected = self.schema_parser.parse(conversation_metadata_detected_str)
        return conversation_metadata_detected

        
