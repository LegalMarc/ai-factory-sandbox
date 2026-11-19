#include <assert.h>

#include "ringbuf.h"

int main(void)
{
    int storage[4];
    struct ringbuf rb;
    int value;
    int i;

    rb_init(&rb, storage, 4);
    assert(rb_len(&rb) == 0);

    assert(rb_pop(&rb, &value) == -1);
    assert(rb_len(&rb) == 0);

    assert(rb_push(&rb, 10) == 0);
    assert(rb_push(&rb, 20) == 0);
    assert(rb_push(&rb, 30) == 0);
    assert(rb_push(&rb, 40) == 0);
    assert(rb_len(&rb) == 4);

    assert(rb_push(&rb, 50) == -1);
    assert(rb_len(&rb) == 4);

    assert(rb_pop(&rb, &value) == 0 && value == 10);
    assert(rb_pop(&rb, &value) == 0 && value == 20);

    assert(rb_push(&rb, 50) == 0);
    assert(rb_push(&rb, 60) == 0);
    assert(rb_push(&rb, 70) == -1);

    assert(rb_pop(&rb, &value) == 0 && value == 30);
    assert(rb_pop(&rb, &value) == 0 && value == 40);
    assert(rb_pop(&rb, &value) == 0 && value == 50);
    assert(rb_pop(&rb, &value) == 0 && value == 60);
    assert(rb_pop(&rb, &value) == -1);
    assert(rb_len(&rb) == 0);

    for (i = 0; i < 100; i++) {
        assert(rb_push(&rb, i) == 0);
        assert(rb_pop(&rb, &value) == 0 && value == i);
    }

    assert(rb_len(&rb) == 0);
    return 0;
}
