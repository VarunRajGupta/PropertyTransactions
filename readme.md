Property Transaction Data Transformation.

As mentioned in design document, there are three major modules in this process - Extract, Transform and Load.
I will split the functions in code among these modules.
  1. Extract - file_validation
  2. Transform - file_key_generation, append_prop_key
  3. Load - create_JSON, get_nested_rec
  
In GCP, serverless data transformation pipelines are created in Dataflow using Apache Beam. Apache Beam is capable of Batch and Stream processing, Data processing is
written as pipeline. We can therefore create a pipeline in Dataflow using ApacheBeam of three steps - Extract , Transform and Load and then will be executed as a pipeline
to generate output.

This existing code as is will not run in apache beam or dataflow it need to updated with Apache Beam steps, moslty coverting this pyhton programem in to a pipeline.

Few more changes will required to make this script run on cloud i.e. instead of reading or writing the files to C or D drive, we will need to do all read/write operations on Bucket.

Pipeline code for Apache Beam will look like this.

import apache_beam as beam

with beam.Pipeline() as pipeline:
	data_processing = (
		pipeline
		|'Extract_CSV' >> file_validation('pp2020.csv')
		|'Transform_Data_1' >> file_key_generation('pp2020.csv',record_count,7,8,3,'pp2020_header.csv')
		|'Transform_Data_2' >> append_prop_key('pp2020_header.csv',prop_key)
		|'Load_JSON' >> create_JSON(data_frame,'pp2020.json')
		)
