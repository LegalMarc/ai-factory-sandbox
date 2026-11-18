#include <assert.h>
#include "ringbuf.h"

int main(void)
{
    int storage[3];
    struct ringbuf rb;
    int v = 0;

    rb_init(&rb, storage, 3);

    assert(rb_len(&rb) == 0);
    assert(rb_pop(&rb, &v) == -1);
    assert(rb_len(&rb) == 0);

    assert(rb_push(&rb, 1) == 0);
    assert(rb_push(&rb, 2) == 0);
    assert(rb_push(&rb, 3) == 0);
    assert(rb_len(&rb) == 3);

    assert(rb_push(&rb, 4) == -1);
    assert(rb_len(&rb) == 3);

    assert(rb_pop(&rb, &v) == 0 && v == 1);
    assert(rb_push(&rb, 5) == 0);
    assert(rb_pop(&rb, &v) == 0 && v == 2);
    assert(rb_pop(&rb, &v) == 0 && v == 3);
    assert(rb_pop(&rb, &v) == 0 && v == 5);
    assert(rb_pop(&rb, &v) == -1);
    assert(rb_len(&rb) == 0);

    assert(rb_push(&rb, 10) == 0);
    assert(rb_push(&rb, 11) == 0);
    assert(rb_push(&rb, 12) == 0);
    assert(rb_pop(&rb, &v) == 0 && v == 10);
    assert(rb_pop(&rb, &v) == 0 && v == 11);
    assert(rb_push(&rb, 13) == 0);
    assert(rb_push(&rb, 14) == 0);
    assert(rb_push(&rb, 15) == -1);
    assert(rb_pop(&rb, &v) == 0 && v == 12);
    assert(rb_pop(&rb, &v) == 0 && v == 13);
    assert(rb_pop(&rb, &v) == 0 && v == 14);
    assert(rb_pop(&rb, &v) == -1);

    return 0;
}
