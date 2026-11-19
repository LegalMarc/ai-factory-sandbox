#include "ringbuf.h"

int main(void)
{
    int storage[3];
    int v = 0;
    struct ringbuf rb;

    rb_init(&rb, storage, 3);
    if (rb_len(&rb) != 0)
        return 1;

    if (rb_pop(&rb, &v) != -1)
        return 1;

    if (rb_push(&rb, 1) != 0 || rb_push(&rb, 2) != 0 ||
        rb_push(&rb, 3) != 0)
        return 1;
    if (rb_len(&rb) != 3)
        return 1;

    if (rb_push(&rb, 4) != -1 || rb_len(&rb) != 3)
        return 1;

    if (rb_pop(&rb, &v) != 0 || v != 1)
        return 1;
    if (rb_push(&rb, 4) != 0)
        return 1;
    if (rb_pop(&rb, &v) != 0 || v != 2)
        return 1;
    if (rb_push(&rb, 5) != 0)
        return 1;
    if (rb_pop(&rb, &v) != 0 || v != 3)
        return 1;
    if (rb_pop(&rb, &v) != 0 || v != 4)
        return 1;
    if (rb_pop(&rb, &v) != 0 || v != 5)
        return 1;
    if (rb_pop(&rb, &v) != -1 || rb_len(&rb) != 0)
        return 1;

    return 0;
}
