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
