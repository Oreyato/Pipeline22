

class PipelineException(Exception):
    """
    A pipeline exception
    """
    pass


if __name__ == "__main__":
    try:
        raise PipelineException("This didn't go as expected")
    except PipelineException as e:
        print(f"Pipeline exception: {e}")
