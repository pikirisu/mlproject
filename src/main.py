from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

if __name__ == "__main__":
    obj = DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    
    print(">>> Before DataTransformation")
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_path,test_path)
    print(">>> After DataTransformation")
