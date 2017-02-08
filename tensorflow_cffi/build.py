from cffi import FFI


ffi = FFI()


ffi.set_source(
    "_tensorflow",
    '#include "tensorflow/c/c_api.h"',
    libraries=[
        "tensorflow",
    ],
)

ffi.cdef(
    """
typedef struct TF_Status TF_Status;
extern TF_Status* TF_NewStatus();
extern void TF_DeleteStatus(TF_Status*);

typedef struct TF_DeprecatedSession TF_DeprecatedSession;

typedef struct TF_Buffer {
  const void* data;
  size_t length;
  void (*data_deallocator)(void* data, size_t length);
} TF_Buffer;

typedef struct TF_Tensor TF_Tensor;

extern void TF_Run(TF_DeprecatedSession*, const TF_Buffer* run_options,
                   const char** input_names, TF_Tensor** inputs, int ninputs,
                   const char** output_names, TF_Tensor** outputs, int noutputs,
                   const char** target_oper_names, int ntargets,
                   TF_Buffer* run_metadata, TF_Status*);
    """,
)


if __name__ == "__main__":
    ffi.compile()
