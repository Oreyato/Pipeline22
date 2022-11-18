

class PipelineException(Exception):
    """
    A pipeline exception
    """

    @staticmethod
    def index_test(max_index, index, func_name):
        try:
            if max_index == -1:
                raise PipelineException("list is empty")
            elif index > max_index or index < 0:
                raise PipelineException("list index out of range")
        except PipelineException as e:
            print(f"Pipeline exception - {func_name}(): {e}")
            return -1


if __name__ == "__main__":
    try:
        raise PipelineException("This didn't go as expected")
    except PipelineException as e:
        print(f"Pipeline exception: {e}")

    PipelineException.index_test(1, 2, "test_func")