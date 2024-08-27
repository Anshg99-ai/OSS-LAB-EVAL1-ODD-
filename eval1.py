{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9169fba7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    }
   ],
   "source": [
    "print(\"hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a3b47a8b",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'if' statement on line 3 (1659247530.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 4\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(i,\"\\n\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after 'if' statement on line 3\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "    print(i,\"\\n\")\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        print(i,\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f2690731",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'if' statement on line 3 (2696412580.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[3], line 4\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(i)\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after 'if' statement on line 3\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "    print(i)\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b4cdc5ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string:Ansh\n",
      "A \n",
      "\n",
      "n \n",
      "\n",
      "s \n",
      "\n",
      "h \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "     print(i,\"\\n\")\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        print(i,\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "35343702",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string:AnshGoel\n",
      "the upper case letters are:\n",
      "A \n",
      "\n",
      "the lower case letters are:\n",
      "the lower case letters are:\n",
      "the lower case letters are:\n",
      "the lower case letters are:\n",
      "G \n",
      "\n",
      "the lower case letters are:\n",
      "the lower case letters are:\n",
      "the lower case letters are:\n",
      "the lower case letters are:\n",
      "n \n",
      "\n",
      "s \n",
      "\n",
      "h \n",
      "\n",
      "o \n",
      "\n",
      "e \n",
      "\n",
      "l \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "print(\"the upper case letters are:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "     print(i,\"\\n\")\n",
    "    print(\"the lower case letters are:\")\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        print(i,\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1a365ce8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string:AnshGoel\n",
      "the upper case letters are:\n",
      "A \n",
      "\n",
      "G \n",
      "\n",
      "the lower case letters are:\n",
      "n \n",
      "\n",
      "s \n",
      "\n",
      "h \n",
      "\n",
      "o \n",
      "\n",
      "e \n",
      "\n",
      "l \n",
      "\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "print(\"the upper case letters are:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "     print(i,\"\\n\")\n",
    "print(\"the lower case letters are:\")\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        print(i,\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "219518e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string:AnshGoel\n",
      "the upper case letters are:\n",
      "G\n",
      "A\n",
      "the lower case letters are:\n",
      "s\n",
      "o\n",
      "n\n",
      "l\n",
      "h\n",
      "e\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "b=set()\n",
    "print(\"the upper case letters are:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "     b.add(i)\n",
    "for i in b:\n",
    "    print(i)\n",
    "c=set()\n",
    "print(\"the lower case letters are:\")\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        c.add(i)\n",
    "for i in c:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3f9462ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the string:AAnssHGoeeLL\n",
      "the upper case letters are:\n",
      "L\n",
      "G\n",
      "A\n",
      "H\n",
      "the lower case letters are:\n",
      "s\n",
      "o\n",
      "e\n",
      "n\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "b=set()\n",
    "print(\"the upper case letters are:\")\n",
    "for i in a:\n",
    "    if(i.isupper()):\n",
    "     b.add(i)\n",
    "for i in b:\n",
    "    print(i)\n",
    "c=set()\n",
    "print(\"the lower case letters are:\")\n",
    "for i in a:\n",
    "    if(i.islower()):\n",
    "        c.add(i)\n",
    "for i in c:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1664ee15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the stringaanshgoel\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'sort'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[12], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m      7\u001b[0m         freq[i]\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m\n\u001b[1;32m----> 8\u001b[0m \u001b[38;5;28mprint\u001b[39m(freq\u001b[38;5;241m.\u001b[39msort())\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'dict' object has no attribute 'sort'"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string\")\n",
    "freq={}\n",
    "for i in a:\n",
    "    if i in freq:\n",
    "        freq[i]=freq[i]+1\n",
    "    else:\n",
    "        freq[i]=1\n",
    "print(freq.sort())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "24868f3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the stringand can man ten\n",
      "n -> 4\n",
      "and -> 1\n"
     ]
    }
   ],
   "source": [
    "a=input(\"enter the string:\")\n",
    "words=a.split()\n",
    "freq={}\n",
    "freq1={}\n",
    "for i in a:\n",
    "    if i in freq and i!=\" \":\n",
    "        freq[i]=freq[i]+1\n",
    "    else:\n",
    "        freq[i]=1\n",
    "c=-1\n",
    "for i in a:\n",
    "    if(freq[i]>c):\n",
    "        s=i\n",
    "        c=freq[i]\n",
    "print(s,\"->\",c)\n",
    "for word in words:\n",
    "    if word in freq1:\n",
    "         freq1[word]=freq1[word]+1\n",
    "    else:\n",
    "        freq1[word]=1\n",
    "d=-1\n",
    "for i in words:\n",
    "    if (freq1[i]>d):\n",
    "        p=i\n",
    "        d=freq1[i]\n",
    "print(p,\"->\",d)  \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fc3972a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
