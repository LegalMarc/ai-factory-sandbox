#include <assert.h>
#include "ringbuf.h"

int main(void)
{
    int storage[3];
    struct ringbuf rb;
    int value = 0;

    rb_init(&rb, storage, 3);
    assert(rb_len(&rb) == 0);

    assert(rb_pop(&rb, &value) == -1);
    assert(rb_len(&rb) == 0);

    assert(rb_push(&rb, 1) == 0);
    assert(rb_push(&rb, 2) == 0);
    assert(rb_push(&rb, 3) == 0);
    assert(rb_len(&rb) == 3);

    assert(rb_push(&rb, 4) == -1);
    assert(rb_len(&rb) == 3);

    assert(rb_pop(&rb, &value) == 0 && value == 1);
    assert(rb_push(&rb, 5) == 0);
    assert(rb_len(&rb) == 3);

    assert(rb_pop(&rb, &value) == 0 && value == 2);
    assert(rb_push(&rb, 6) == 0);

    assert(rb_pop(&rb, &value) == 0 && value == 3);
    assert(rb_pop(&rb, &value) == 0 && value == 5);
    assert(rb_pop(&rb, &value) == 0 && value == 6);
    assert(rb_pop(&rb, &value) == -1);
    assert(rb_len(&rb) == 0);

    return 0;
}
