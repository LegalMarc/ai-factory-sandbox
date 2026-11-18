#include "ringbuf.h"

#include <assert.h>
#include <stddef.h>

int main(void)
{
    int storage[3];
    struct ringbuf rb;
    int value;

    rb_init(&rb, storage, 3);
    assert(rb_len(&rb) == 0);

    assert(rb_pop(&rb, &value) == -1);

    assert(rb_push(&rb, 10) == 0);
    assert(rb_push(&rb, 20) == 0);
    assert(rb_push(&rb, 30) == 0);
    assert(rb_len(&rb) == 3);

    assert(rb_push(&rb, 40) == -1);
    assert(rb_len(&rb) == 3);

    assert(rb_pop(&rb, &value) == 0);
    assert(value == 10);

    assert(rb_push(&rb, 40) == 0);
    assert(rb_len(&rb) == 3);

    assert(rb_pop(&rb, &value) == 0);
    assert(value == 20);
    assert(rb_pop(&rb, &value) == 0);
    assert(value == 30);
    assert(rb_pop(&rb, &value) == 0);
    assert(value == 40);

    assert(rb_pop(&rb, &value) == -1);
    assert(rb_len(&rb) == 0);

    assert(rb_push(&rb, 50) == 0);
    assert(rb_push(&rb, 60) == 0);
    assert(rb_pop(&rb, &value) == 0);
    assert(value == 50);
    assert(rb_push(&rb, 70) == 0);
    assert(rb_push(&rb, 80) == 0);
    assert(rb_push(&rb, 90) == -1);

    assert(rb_pop(&rb, &value) == 0);
    assert(value == 60);
    assert(rb_pop(&rb, &value) == 0);
    assert(value == 70);
    assert(rb_pop(&rb, &value) == 0);
    assert(value == 80);
    assert(rb_pop(&rb, &value) == -1);

    return 0;
}
